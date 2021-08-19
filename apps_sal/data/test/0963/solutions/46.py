(N, K) = map(int, input().split())
rng = [list(map(int, input().split())) for i in range(K)]
dp = [0] * (N + 1)
dp[1] = 1
s = [0] * (N + 1)
s[1] = 1
MOD = 998244353
for i in range(2, N + 1):
    for (j, k) in rng:
        if i - j < 1:
            pass
        elif i - k < 1:
            k = i - 1
        dp[i] += s[i - j] - s[i - k - 1]
        dp[i] %= MOD
    s[i] += (s[i - 1] + dp[i]) % MOD
print(dp[-1])
