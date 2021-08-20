(n, m, k) = list(map(int, input().split()))
mod = 998244353
dp = [[0] * (k + 1) for i in range(n)]
dp[0][0] = m
for i in range(1, n):
    for j in range(k + 1):
        dp[i][j] = dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] * (m - 1)
        dp[i][j] %= mod
print(dp[n - 1][k])
