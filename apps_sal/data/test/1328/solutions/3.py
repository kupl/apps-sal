(N, Ma, Mb) = map(int, input().split())
INF = 40 * 100 + 1
dp = [[INF for i in range(10 * N + 1)] for j in range(10 * N + 1)]
dp[0][0] = 0
ans = INF
for p in range(N):
    (a, b, c) = map(int, input().split())
    for i in range(len(dp) - 1, -1, -1):
        for j in range(len(dp[i]) - 1, -1, -1):
            if dp[i][j] != INF:
                dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)
                if (i + a) / (j + b) == Ma / Mb:
                    ans = min(ans, dp[i + a][j + b])
if ans == INF:
    print(-1)
else:
    print(ans)
