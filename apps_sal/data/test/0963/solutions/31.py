N, K = map(int, input().split())
MOD = 998244353
L = [0] * K
R = [0] * K
for i in range(K):
    L[i], R[i] = map(int, input().split())

dp = [0] * (N + 1)
dp[1] = 1

for i in range(1, N):
    for e in range(K):
        left = max(0, i - R[e])
        right = max(0, i - L[e] + 1)
        dp[i + 1] += dp[right] - dp[left]
    dp[i + 1] += dp[i]
    dp[i + 1] %= MOD
print((dp[N] - dp[N - 1]) % MOD)
