n, z, w = list(map(int, input().split()))
a = list(map(int, input().split()))
INF = 10 ** 10

dp = [[None] * 2 for _ in range(n)]
for i in range(n - 1, -1, -1):
    dp[i][0] = -INF
    y = a[i - 1] if i else w
    dp[i][0] = max(dp[i][0], abs(y - a[-1]))
    for j in range(i + 1, n):
        dp[i][0] = max(dp[i][0], dp[j][1])

    dp[i][1] = INF
    x = a[i - 1] if i else z
    dp[i][1] = min(dp[i][1], abs(x - a[-1]))
    for j in range(i + 1, n):
        dp[i][1] = min(dp[i][1], dp[j][0])

ans = dp[0][0]
print(ans)
