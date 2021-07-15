N, K = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(K)]

mod = 998244353
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    for l, r in lr:
        if i-l < 1:
            continue
        dp[i] += dp[i-l]-dp[max(i-r-1, 0)]
    dp[i] += dp[i-1]
    dp[i] %= mod

print((dp[N]-dp[N-1])%mod)
