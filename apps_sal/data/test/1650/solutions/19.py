mod = 10 ** 9 + 7
s = input()
n = len(s)
dp = [[0] * 2 for _ in range(100001)]
dp[0][0] = 1
for i in range(n):
    if s[i] == '0':
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % mod
    if s[i] == '0':
        dp[i + 1][1] += dp[i][1] * 2 % mod
    else:
        dp[i + 1][0] += dp[i][0] * 2 % mod
        dp[i + 1][1] += dp[i][1] * 2 % mod
print((dp[n][0] + dp[n][1]) % mod)
