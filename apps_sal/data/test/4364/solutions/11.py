N = input()
A = int(N[:2])
B = int(N[2:])
if (A >= 1 and A <=12):
    if (B >= 1 and B <=12):
        print('AMBIGUOUS')
    else:
        print('MMYY')

else:
    if (B >= 1 and B <=12):
        print('YYMM')
    else:
        print('NA')
