N = int(input())
s = bin(N)[2:]
n = len(s)
dp = [[0] * 4 for i in range(len(s)+1)]
dp[0][0] = 1
MOD = int(1e9) + 7
for i in range(n):
    b = 1 if s[i] == '1' else 0
    for j in range(4):
        for k in range(3):
            nj = min(((j << 1) + b - k, 3))
            if 0 <= nj:
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD
print((sum(dp[n]) % MOD))

