s = input()

if 0 < int(s[:2]) <= 12:
    if 0 < int(s[2:]) <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 0 < int(s[2:]) <= 12:
        print('YYMM')
    else:
        print('NA')
