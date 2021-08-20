S = int(input())
A = S // 100
B = S % 100
if 0 < A <= 12 and 0 < B <= 12:
    print('AMBIGUOUS')
elif 0 < A <= 12:
    print('MMYY')
elif 0 < B <= 12:
    print('YYMM')
else:
    print('NA')
