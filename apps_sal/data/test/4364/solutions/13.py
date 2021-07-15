S = input()
months = set([str(i).zfill(2) for i in range(1, 13)])

res = ''
if S[:2] in months and S[2:] in months:
    res = 'AMBIGUOUS'
elif S[:2] in months:
    res = 'MMYY'
elif S[2:] in months:
    res = 'YYMM'
else:
    res = 'NA'

print(res)
