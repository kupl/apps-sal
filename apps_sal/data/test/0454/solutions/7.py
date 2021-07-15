import sys

MOD = 10**9 + 7

N, K = list(map(int, input().split()))

maxS = N*N//2
if K > maxS or K%2:
    print((0))
    return

dp = [[0]*(maxS+1) for j in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    dp2 = [[0]*(maxS+1) for j in range(N+1)]
    for j in range(i+1):
        for s in range(0, maxS+1, 2):
            s0 = s-2*j
            if s0 < 0: continue
            dp2[j][s] = (2*j+1)*dp[j][s0]
            if j+1 <= N:
                dp2[j][s] += (j+1)*(j+1)*dp[j+1][s0]
            if j-1 >= 0:
                dp2[j][s] += dp[j-1][s0]
            dp2[j][s] %= MOD
    dp = dp2

print((dp[0][K]))

