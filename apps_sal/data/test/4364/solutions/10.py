s = int(input())
l, r = s / 100, s % 100
if 1 <= l <= 12:
    if 1 <= r <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 1 <= r <= 12:
    print('YYMM')
else:
    print('NA')
