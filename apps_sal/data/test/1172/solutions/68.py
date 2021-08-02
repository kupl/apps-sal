MOD = 10**9 + 7

S = input()
N = len(S)
dp = [[0] * 4 for i in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    s = S[i]
    for j in range(4):
        if s == "?":
            dp[i + 1][j] += dp[i][j] * 3 % MOD
        else:
            dp[i + 1][j] += dp[i][j] % MOD
        if j < 3 and (s == "?" or s == "ABC"[j]):
            dp[i + 1][j + 1] += dp[i][j] % MOD
print((dp[N][3] % MOD))
