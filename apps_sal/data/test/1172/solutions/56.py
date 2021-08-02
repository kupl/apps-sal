MOD = pow(10, 9) + 7
s = input()
n = len(s)
dp = [[0 for _ in range(4)] for _ in range(n + 1)]

dp[0][0] = 1
for i in range(n):
    dp[i + 1][0] = dp[i][0]
    dp[i + 1][1] = dp[i][1]
    dp[i + 1][2] = dp[i][2]
    dp[i + 1][3] = dp[i][3]
    if s[i] == 'A':
        dp[i + 1][1] += dp[i][0]
    elif s[i] == 'B':
        dp[i + 1][2] += dp[i][1]
    elif s[i] == 'C':
        dp[i + 1][3] += dp[i][2]
    else:
        dp[i + 1][0] = dp[i][0] * 3
        dp[i + 1][1] = dp[i][1] * 3
        dp[i + 1][2] = dp[i][2] * 3
        dp[i + 1][3] = dp[i][3] * 3
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][2] += dp[i][1]
        dp[i + 1][3] += dp[i][2]
    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD
    dp[i + 1][2] %= MOD
    dp[i + 1][3] %= MOD

print((dp[n][3]))
