S = input()
a = 1 <= int(S[:2]) <= 12
b = 1 <= int(S[-2:]) <= 12
if a & b:
    print('AMBIGUOUS')
elif a:
    print('MMYY')
elif b:
    print('YYMM')
else:
    print('NA')
