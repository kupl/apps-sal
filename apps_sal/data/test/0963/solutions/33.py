(N, K) = map(int, input().split())
MOD = 998244353
LR = [list(map(int, input().split())) for _ in range(K)]
dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 1
prefix_sum = [0] * (N + 1)
prefix_sum[1] = 1
for i in range(2, N + 1):
    for j in range(K):
        (l, r) = LR[j]
        l1 = max(i - r - 1, 0)
        r1 = max(i - l, 0)
        dp[i] += prefix_sum[r1] - prefix_sum[l1]
        dp[i] %= MOD
    prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD
print(dp[-1])
