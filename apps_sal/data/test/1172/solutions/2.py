mod = 10 ** 9 + 7
s = input()
dp = [[0] * 4 for i in range(len(s) + 1)]
dp[len(s)][3] = 1
for i in range(len(s))[::-1]:
    for j in range(4)[::-1]:
        if s[i] == "?":
            dp[i][j] = dp[i + 1][j] * 3
        else:
            dp[i][j] = dp[i + 1][j]
        if j < 3:
            if s[i] == "?" or s[i] == "ABC"[j]:
                dp[i][j] += dp[i + 1][j + 1]
        dp[i][j] %= mod
print(dp[0][0])
