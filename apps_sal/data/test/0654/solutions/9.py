N = int(input())
mod = 10**9+7
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1
for i in range(2, N+1):
    if i % 2:
        dp[i][i] = 1 + i//2
    else:
        dp[i][i] = i//2
    for j in range(i-1, -1, -1):
        dp[i][j] = (dp[i][j+1] + dp[i-1][j-1] + j%2)%mod
print(dp[-1][0])
