S = input().strip()
a = int(S[:2])
b = int(S[2:])
aa = a < 13 and a != 0
bb = b < 13 and b != 0

if aa and bb:
    ans = 'AMBIGUOUS'
elif aa and not bb:
    ans = 'MMYY'
elif bb and not aa:
    ans = 'YYMM'
else:
    ans = 'NA'
print(ans)
