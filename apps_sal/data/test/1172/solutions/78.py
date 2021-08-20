s = input()
n = len(s)
mod = 10 ** 9 + 7
dp = [[0] * 4 for i in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    l = s[i]
    for j in range(4):
        if l == '?':
            dp[i + 1][j] = dp[i][j] * 3 % mod
        else:
            dp[i + 1][j] = dp[i][j] % mod
    if l == 'A' or l == '?':
        dp[i + 1][1] += dp[i][0] % mod
    if l == 'B' or l == '?':
        dp[i + 1][2] += dp[i][1] % mod
    if l == 'C' or l == '?':
        dp[i + 1][3] += dp[i][2] % mod
print(dp[n][3] % mod)
