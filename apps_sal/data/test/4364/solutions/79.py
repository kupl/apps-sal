S = int(input())

L = S // 100
R = S % 100

if L > 12 or L == 0:
    if R > 12 or R == 0:
        print('NA')
    else:
        print('YYMM')
else:
    if R > 12 or R == 0:
        print('MMYY')
    else:
        print('AMBIGUOUS')
