(N, ma, mb) = list(map(int, input().split()))
a = [0] * N
b = [0] * N
c = [0] * N
NMAX = 40
ABMAX = 10
INF = 1000000
for i in range(N):
    (a[i], b[i], c[i]) = list(map(int, input().split()))
dp = [[[INF] * (NMAX * ABMAX + 1) for _ in range(NMAX * ABMAX + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for ca in range(NMAX * ABMAX + 1):
        for cb in range(NMAX * ABMAX + 1):
            if dp[i][ca][cb] == INF:
                continue
            dp[i + 1][ca][cb] = min(dp[i + 1][ca][cb], dp[i][ca][cb])
            dp[i + 1][ca + a[i]][cb + b[i]] = min(dp[i + 1][ca + a[i]][cb + b[i]], dp[i][ca][cb] + c[i])
ans = INF
for ca in range(1, NMAX * ABMAX + 1):
    for cb in range(1, NMAX * ABMAX + 1):
        if ca * mb == cb * ma:
            ans = min(ans, dp[N][ca][cb])
print(ans if ans != INF else -1)
