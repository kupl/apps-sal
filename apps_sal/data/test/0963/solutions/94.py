MOD = 998244353
(N, K) = list(map(int, input().split()))
LR_K = [list(map(int, input().split())) for _ in range(K)]
S = set()
for LR in LR_K:
    S |= set(range(LR[0], LR[1] + 1))
dp = [0] * (N + 1)
dp[1] = 1
dpsum = [0] * (N + 1)
dpsum[1] = 1
for i in range(2, N + 1):
    for LR in LR_K:
        li = max(i - LR[1], 1)
        ri = i - LR[0]
        if ri < 0:
            continue
        dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= MOD
    dpsum[i] = dpsum[i - 1] + dp[i]
print(dp[N])
