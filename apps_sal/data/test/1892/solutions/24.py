MOD = 1000000007
n = int(input())
p = ''.join([input() for _ in range(n)])
dp = [[0] * 5005 for _ in range(n + 1)]
dp[0][0] = 1
i = 1
for c in p:
    if c == 'f':
        for j in range(n - 1, -1, -1):
            dp[i][j] = dp[i - 1][j - 1] if j - 1 >= 0 else 0
    else:
        for j in range(n - 1, -1, -1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j + 1]) % MOD
    i += 1
print(dp[n][0] % MOD)
