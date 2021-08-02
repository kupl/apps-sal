n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
bef = sum(aa)
for i in range(n):
    aa[i] -= bb[i]
    if aa[i] >= 0:
        bb[i] = 0
    else:
        bb[i] = 0 - aa[i]
        aa[i] = 0
    aa[i + 1] -= bb[i]
    if aa[i + 1] >= 0:
        bb[i] = 0
    else:
        bb[i] = 0 - aa[i + 1]
        aa[i + 1] = 0
print((bef - sum(aa)))
