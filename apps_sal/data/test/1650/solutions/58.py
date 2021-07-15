L = input()
N = len(L)
MOD = 10**9+7

dp = [[0,0] for i in range(N+1)]
dp[0][0] = 1
for i,a in enumerate(L):
    a = int(a)
    for less in range(2):
        for d in range(2):
            if less==0 and d > a: continue
            nl = int(less or d < a)
            dp[i+1][nl] += dp[i][less] * (d+1)
    dp[i+1][0] %= MOD
    dp[i+1][1] %= MOD

print(sum(dp[-1]) % MOD)
