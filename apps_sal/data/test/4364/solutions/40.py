s = list(input())
s = [int(i + j) for (i, j) in zip(s[::2], s[1::2])]
if 1 <= s[0] <= 12:
    if 1 <= s[1] <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 1 <= s[1] <= 12:
    print('YYMM')
else:
    print('NA')
