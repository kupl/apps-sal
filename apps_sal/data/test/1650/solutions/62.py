l = input()
n = len(l)
mod = 10 ** 9 + 7
dp = [[0 for i in range(2)] for j in range(n + 1)]
dp[0][1] = 1
for i in range(n):
    if l[i] == "1":
        dp[i + 1][0] = dp[i][0] * 3 + dp[i][1]
        dp[i + 1][0] %= mod
        dp[i + 1][1] = dp[i][1] * 2
        dp[i + 1][1] %= mod
    else:
        dp[i + 1][0] = dp[i][0] * 3
        dp[i + 1][0] %= mod
        dp[i + 1][1] = dp[i][1]
        dp[i + 1][1] %= mod
print((dp[n][0] + dp[n][1]) % mod)
