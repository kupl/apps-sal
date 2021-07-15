N = list(map(int, list(input())))
L = len(N)
K = int(input())
 
dp = [[[0] * (K+1) for j in range(2)] for i in range(L+1)]
dp[0][0][0] = 1
 
for i in range(L):
    ni = N[i]
    if ni == 0:
        for j in range(K):
            dp[i+1][1][j+1] += dp[i][1][j] * 9
        for j in range(K+1):
            dp[i+1][0][j] += dp[i][0][j]
    else:
        for j in range(K+1):
            dp[i+1][1][j] += dp[i][0][j]
        for j in range(K):
            dp[i+1][1][j+1] += (dp[i][0][j] * (ni-1) + dp[i][1][j] * 9)
            dp[i+1][0][j+1] += dp[i][0][j]
 
    for j in range(K+1):
        dp[i+1][1][j] += dp[i][1][j]
 
print(dp[L][0][K]+dp[L][1][K])
