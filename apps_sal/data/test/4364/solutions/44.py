s = input()
if s[0:2] in '01 02 03 04 05 06 07 08 09 10 11 12':
    l = 'm'
else:
    l = 'y'
if s[2:4] in '01 02 03 04 05 06 07 08 09 10 11 12':
    r = 'm'
else:
    r = 'y'
if l + r == 'mm':
    print('AMBIGUOUS')
elif l + r == 'my':
    print('MMYY')
elif l + r == 'ym':
    print('YYMM')
else:
    print('NA')
