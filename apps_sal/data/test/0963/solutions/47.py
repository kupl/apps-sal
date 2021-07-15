N, K, *LR = list(map(int, open(0).read().split()))
MOD = 998244353
dp = [0] * N
acc = [0] * (N + 1)
dp[0] = 1
acc[1] = 1
for i in range(N):
    for l, r in zip(*[iter(LR)] * 2):
        left = max(0, i - r)
        right = max(0, i - l + 1)
        dp[i] += acc[right] - acc[left]
        dp[i] %= MOD
    acc[i + 1] = acc[i] + dp[i]
    acc[i + 1] %= MOD
print((dp[-1]))

