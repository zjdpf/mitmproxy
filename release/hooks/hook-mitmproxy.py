hiddenimports = ["mitmproxy.script"]

# taken from https://github.com/pyinstaller/pyinstaller/blob/develop/PyInstaller/hooks/hook-pkg_resources.py
# at 2020-05-01, required for PyInstaller < 3.7
hiddenimports.append('pkg_resources.py2_warn')