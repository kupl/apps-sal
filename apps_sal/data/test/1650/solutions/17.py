s = input()[::-1]
n = len(s)
mod = 10**9 + 7
dp = [[0] * 2 for i in range(n + 5)]

dp[n][0] = 1
for i in reversed(range(n)):
    if s[i] == '0':
        dp[i][0] = dp[i + 1][0]
        dp[i][1] = dp[i + 1][1]
    else:
        dp[i][1] = (dp[i + 1][1] + dp[i + 1][0]) % mod

    if s[i] == '0':
        dp[i][1] += dp[i + 1][1] * 2
        dp[i][1] %= mod
    else:
        dp[i][0] += dp[i + 1][0] * 2
        dp[i][0] %= mod
        dp[i][1] += dp[i + 1][1] * 2
        dp[i][1] %= mod

print((dp[0][0] + dp[0][1]) % mod)
