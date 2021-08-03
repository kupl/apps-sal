MOD = 10 ** 9 + 7
N = int(input())
M = len(bin(N)) - 2
L = bin(N)[2:]

dp = [[0] * 3 for _ in range(M + 1)]
dp[0][0] = 1

for i in range(M):
    if L[i] == '1':
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][1] += dp[i][0] + dp[i][1]
        dp[i + 1][2] += 2 * dp[i][1] + 3 * dp[i][2]
    else:
        dp[i + 1][0] += dp[i][0] + dp[i][1]
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][2] += dp[i][1] + 3 * dp[i][2]

    for j in range(3):
        dp[i + 1][j] %= MOD


print((sum(dp[M]) % MOD))
