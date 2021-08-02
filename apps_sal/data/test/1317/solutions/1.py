n, m = list(map(int, input().split()))
nOfM = [0 for i in range(m)]
for md in range(m):
    if md <= n:
        nOfM[md] = (n - md) // m
        if md != 0:
            nOfM[md] += 1
res = 0
for m1 in range(m):
    for m2 in range(m):
        if (m1 * m1 + m2 * m2) % m == 0:
            res += nOfM[m1] * nOfM[m2]
print(res)
