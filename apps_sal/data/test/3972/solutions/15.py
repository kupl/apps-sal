n = int(input())
dp = [0] * (n + 1)
mod = 10**9 + 7
dp[0] = n
dp[1] = n * n
SUM = n + n * n
for i in range(2, n):
    dp[i] = (n - 1) * (n - 1) + n - i + 1 + SUM - dp[i - 2]
    dp[i] %= mod
    SUM += dp[i]
    SUM %= mod
print(dp[n - 1])
