n = int(input())
lsr = list(map(int, input().split()))
ls = [lsr[0]]
for le in lsr[1:]:
    if le != ls[-1]:
        ls.append(le)
n = len(ls)
dpa = []
dpb = [0 for i in range(n + 1)]
for sz in range(2, n + 1):
    dp = []
    for start in range(n - sz + 1):
        if ls[start] == ls[start + sz - 1]:
            dp.append(min(dpb[start], dpb[start + 1], dpa[start + 1]) + 1)
        else:
            dp.append(min(dpb[start], dpb[start + 1]) + 1)
    (dpa, dpb) = (dpb, dp)
print(dpb[0])
