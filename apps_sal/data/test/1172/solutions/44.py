s = input()
n = len(s)
MOD = 10 ** 9 + 7
dp = [[0] * 4 for _ in range(n + 1)]
dp[0][0] = 1

for i, x in enumerate(s):
    if x == 'A' or x == '?':
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][2] += dp[i][2]
        dp[i + 1][3] += dp[i][3]
        dp[i + 1][1] += dp[i][0]
    if x == 'B' or x == '?':
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][2] += dp[i][2]
        dp[i + 1][3] += dp[i][3]
        dp[i + 1][2] += dp[i][1]
    if x == 'C' or x == '?':
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][2] += dp[i][2]
        dp[i + 1][3] += dp[i][3]
        dp[i + 1][3] += dp[i][2]

    for j in range(4):
        dp[i + 1][j] %= MOD

print((dp[n][3]))
