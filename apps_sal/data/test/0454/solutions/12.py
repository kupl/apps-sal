MOD = 10**9 + 7
n, oddness = [int(item) for item in input().split()]
# Oddness must be even
if oddness % 2 ==  1:
    print(0)
    return
oddness //= 2
max_oddness = 1300 + n
max_pending = n//2 + 2

dp = [[[0] * (max_oddness) for _ in range(max_pending)] for _ in range(n)]
dp[0][0][0] = 1
dp[0][1][1] = 1
for i in range(1, n):
    for j in range(min(i+1, max_pending-1)):
        for k in range(oddness+1):
            dp_ijk = dp[i-1][j][k]
            # Oddness increase by num of pending item
            # Connect in line or Choose 1 from pending items
            dp[i][j][k+j] += dp_ijk * (1 + j*2)
            dp[i][j][k+j] %= MOD
            # Choose 2 from pending items
            if j > 0:
                dp[i][j-1][k+j-1] += dp_ijk * j*j
            # Do nothing 
            dp[i][j+1][k+j+1] += dp_ijk 

print(dp[n-1][0][oddness] % MOD)
