dp = [[0 for i in range(2005)]for i in range(2005)]
n, p, t = 0, 0, 0
n, p, t = map(float, input().split())
n, t = int(n), int(t)
dp[0][0] = 1
for i in range(1, t + 1):
    for j in range(n + 1):
        if j == n:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] * (1 - p)
        if j:
            dp[i][j] += dp[i - 1][j - 1] * p
ans = 0
for i in range(n + 1):
    ans += i * dp[t][i]
print(ans)
