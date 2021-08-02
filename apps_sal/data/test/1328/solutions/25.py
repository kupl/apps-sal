NMAX = 40
ABMAX = 10
INF = 1000000
N, MA, MB = list(map(int, input().split()))
A = [0] * NMAX
B = [0] * NMAX
C = [0] * NMAX
dp = [[[INF for _ in range(NMAX * ABMAX + 1)] for _ in range(NMAX * ABMAX + 1)] for _ in range(NMAX + 1)]
for i in range(N):
    A[i], B[i], C[i] = list(map(int, input().split()))

dp[0][0][0] = 0
for i in range(N):
    for ca in range(NMAX * ABMAX + 1):
        for cb in range(NMAX * ABMAX + 1):
            if dp[i][ca][cb] == INF:
                continue
            dp[i + 1][ca][cb] = min(dp[i + 1][ca][cb], dp[i][ca][cb])
            dp[i + 1][ca + A[i]][cb + B[i]] = min(dp[i + 1][ca + A[i]][cb + B[i]], dp[i][ca][cb] + C[i])

ans = INF
for ca in range(1, NMAX * ABMAX + 1):
    for cb in range(1, NMAX * ABMAX + 1):
        if ca * MB == cb * MA:
            ans = min(ans, dp[N][ca][cb])
if ans == INF:
    ans = -1
print(ans)
