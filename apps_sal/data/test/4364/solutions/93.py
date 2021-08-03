import re

s = input()


def is_valid_yymm(s):
    match = re.search('^[0-9]{2}(01|02|03|04|05|06|07|08|09|10|11|12)$', s)
    return bool(match)


def is_valid_mmyy(s):
    match = re.search('^(01|02|03|04|05|06|07|08|09|10|11|12)[0-9]{2}$', s)
    return bool(match)


if is_valid_yymm(s) and is_valid_mmyy(s):
    print('AMBIGUOUS')
elif is_valid_yymm(s):
    print('YYMM')
elif is_valid_mmyy(s):
    print('MMYY')
else:
    print('NA')
