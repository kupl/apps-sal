S = input()
x = int(S[:2])
y = int(S[2:4])
if 1 <= x <= 12:
    if 1 <= y <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 1 <= y <= 12:
    print('YYMM')
else:
    print('NA')
