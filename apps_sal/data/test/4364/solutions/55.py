s = input()
if 12 < int(s[:2]) or 0 == int(s[:2]):
    if 12 >= int(s[2:]) >= 1:
        print('YYMM')
    else:
        print('NA')
elif 1 <= int(s[:2]) <= 12:
    if 12 >= int(s[2:]) >= 1:
        print('AMBIGUOUS')
    else:
        print('MMYY')
