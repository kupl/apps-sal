MOD = 10**9 + 7
L = input()
K = len(L)
dp = [[0, 0] for i in range(K + 1)]
dp[0][0] = 1
for i in range(K):
    if(L[i] == '0'):
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1] * 3 % MOD
    elif(L[i] == '1'):
        dp[i + 1][0] = dp[i][0] * 2 % MOD
        dp[i + 1][1] = (dp[i][1] * 3 % MOD + dp[i][0]) % MOD
print(sum(dp[K]) % MOD)
