mod = 10**9 + 7
s = input()
n = len(s)
dp = [[0] * 4 for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] * ((s[i - 1] == "?") * 2 + 1)
    dp[i][1] = dp[i - 1][1] * ((s[i - 1] == "?") * 2 + 1)
    dp[i][2] = dp[i - 1][2] * ((s[i - 1] == "?") * 2 + 1)
    dp[i][3] = dp[i - 1][3] * ((s[i - 1] == "?") * 2 + 1)
    if s[i - 1] == "A" or s[i - 1] == "?":
        dp[i][1] += dp[i - 1][0]
    if s[i - 1] == "B" or s[i - 1] == "?":
        dp[i][2] += dp[i - 1][1]
    if s[i - 1] == "C" or s[i - 1] == "?":
        dp[i][3] += dp[i - 1][2]
    dp[i][0] %= mod
    dp[i][1] %= mod
    dp[i][2] %= mod
    dp[i][3] %= mod
print(dp[n][3])
