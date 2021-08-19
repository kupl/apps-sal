mod = 10 ** 9 + 7
S = input()
s = len(S)
dp = [[0 for i in range(4)] for j in range(s + 1)]
mod = 10 ** 9 + 7
dp[0][0] = 1
for j in range(4):
    for i in range(s):
        dp[i + 1][j] = dp[i][j] % mod
        if S[i] == '?':
            dp[i + 1][j] = dp[i][j] * 3 % mod
            if j > 0:
                dp[i + 1][j] += dp[i][j - 1] % mod
        elif 'ABC'.index(S[i]) + 1 == j:
            dp[i + 1][j] += dp[i][j - 1] % mod
print(dp[s][3] % mod)
