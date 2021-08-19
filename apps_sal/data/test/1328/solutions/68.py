(N, ma, mb) = map(int, input().split())
(a, b, c) = ([0] * N, [0] * N, [0] * N)
for i in range(N):
    (a[i], b[i], c[i]) = map(int, input().split())
MA = sum(a)
MB = sum(b)
dp = [[[float('inf') for i in range(MB + 1)] for j in range(MA + 1)] for k in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(MA):
        for k in range(MB):
            if dp[i][j][k] == float('inf'):
                continue
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][j + a[i]][k + b[i]] = min(dp[i + 1][j + a[i]][k + b[i]], dp[i][j][k] + c[i])
ans = float('inf')
for i in range(1, MA + 1):
    for j in range(1, MB + 1):
        if i * mb == j * ma:
            ans = min(ans, dp[N][i][j])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
