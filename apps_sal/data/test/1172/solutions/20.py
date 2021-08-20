s = input()
mod = 10 ** 9 + 7
dp = [[0] * 4 for i in range(len(s) + 1)]
dp[0][0] = 1
for i in range(len(s)):
    if s[i] == 'A':
        dp[i + 1][1] += dp[i][0]
    elif s[i] == 'B':
        dp[i + 1][2] += dp[i][1]
    elif s[i] == 'C':
        dp[i + 1][3] += dp[i][2]
    else:
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][2] += dp[i][1]
        dp[i + 1][3] += dp[i][2]
    for j in range(4):
        if s[i] == '?':
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * 3) % mod
        else:
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
print(dp[-1][3] % mod)
