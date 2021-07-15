s = input()
a = int(s[0:2])
b = int(s[2:])

if 13 <= a or a == 0:
    if 1 <= b and b <= 12:
        print('YYMM')
    else:
        print('NA')
else:
    
    if 1<= b  and b<= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
