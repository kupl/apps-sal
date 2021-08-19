(nmax, abmax, inf) = (40, 10, 1000000)
dp = [[[inf] * (nmax * abmax + 1) for _ in range(nmax * abmax + 1)] for _ in range(nmax + 1)]
(n, ma, mb) = list(map(int, input().split()))
dp[0][0][0] = 0
for i in range(n):
    (a, b, c) = list(map(int, input().split()))
    dpi = dp[i]
    dpi1 = dp[i + 1]
    for ca in range(0, 401):
        for cb in range(0, 401):
            if dpi[ca][cb] == inf:
                continue
            dpi1[ca][cb] = min(dpi1[ca][cb], dpi[ca][cb])
            dpi1[ca + a][cb + b] = min(dpi1[ca + a][cb + b], dpi[ca][cb] + c)
ans = inf
dpn = dp[n]
for ca in range(1, 401):
    for cb in range(1, 401):
        if ca * mb == cb * ma:
            ans = min(ans, dpn[ca][cb])
if ans == inf:
    ans = -1
print(ans)
