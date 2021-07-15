H,W,K = map(int,input().split())
dp = [[0]*W for i in range(H+1)]
dp[0][0] = 1
MOD = 10**9+7
for i in range(H):
    for b in range(1<<(W-1)):
        if '11' in bin(b): continue
        for k in range(W):
            if k and b&(1<<(k-1)):
                dp[i+1][k-1] += dp[i][k]
            elif b&(1<<k):
                dp[i+1][k+1] += dp[i][k]
            else:
                dp[i+1][k] += dp[i][k]
print(dp[-1][K-1] % MOD)
