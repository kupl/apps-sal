L = input()
lenl = len(L)
MOD = 10 ** 9 + 7
dp = [[0] * len(L) for _ in range(2)]
dp[0][0] = 2
dp[1][0] = 1
for i in range(1, len(L)):
    b = L[i]
    if b == '1':
        dp[0][i] = dp[0][i - 1] * 2
        dp[1][i] = dp[0][i - 1] + dp[1][i - 1] * 3
    else:
        dp[0][i] = dp[0][i - 1]
        dp[1][i] = dp[1][i - 1] * 3
    dp[0][i] %= MOD
    dp[1][i] %= MOD
print((dp[0][-1] + dp[1][-1]) % MOD)
