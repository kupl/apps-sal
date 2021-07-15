S = input()
N = len(S)
dp = [[0 for _ in range(4)] for _ in range(N+1)]
dp[0][0] = 1
MOD = 10 ** 9 + 7

for i in range(N):
    if S[i] == 'A':
        dp[i+1][0] = dp[i][0] % MOD
        dp[i+1][1] = (dp[i][0] + dp[i][1]) % MOD
        dp[i+1][2] = dp[i][2] % MOD
        dp[i+1][3] = dp[i][3] % MOD
     
    if S[i] == 'B':
        dp[i+1][0] = dp[i][0] % MOD
        dp[i+1][1] = dp[i][1] % MOD
        dp[i+1][2] = (dp[i][1] + dp[i][2]) % MOD
        dp[i+1][3] = dp[i][3] % MOD
    
    if S[i] == 'C':
        dp[i+1][0] = dp[i][0] % MOD
        dp[i+1][1] = dp[i][1] % MOD
        dp[i+1][2] = dp[i][2] % MOD
        dp[i+1][3] = (dp[i][2] + dp[i][3]) % MOD
    
    if S[i] == '?':
        dp[i+1][0] = 3 * dp[i][0] % MOD
        dp[i+1][1] = (dp[i][0] + 3 * dp[i][1]) % MOD
        dp[i+1][2] = (dp[i][1] + 3 * dp[i][2]) % MOD
        dp[i+1][3] = (dp[i][2] + 3 * dp[i][3]) % MOD

print(dp[N][3] % MOD)
