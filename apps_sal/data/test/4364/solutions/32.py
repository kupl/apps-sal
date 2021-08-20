S = input()
f = int(S[:2])
l = int(S[2:])
if f == 0 or f > 12:
    if l == 0 or l > 12:
        print('NA')
    else:
        print('YYMM')
elif l == 0 or l > 12:
    print('MMYY')
else:
    print('AMBIGUOUS')
