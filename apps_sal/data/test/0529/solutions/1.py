_27 = input()
_16 = int(input())
_27 = _27.lower()
_4 = ""
for _26 in range(len(_27)):
    _19 = _27[_26]
    if ord(_19) < _16 + 97:
        _4 = _4 + _19.upper()
    else:
        _4 = _4 + _19.lower()
print(_4)

