N, K = map(int, input().split())
K = min(N - 1, K)
fact = [1 for _ in range(200001)]
inv = [1 for _ in range(200001)]
fact_inv = [1 for _ in range(200001)]
mod = 10**9 + 7
for i in range(2, 200001):
    fact[i] = (fact[i - 1] * i) % mod
    inv[i] = mod - (inv[mod % i] * (mod // i)) % mod
    fact_inv[i] = (fact_inv[i - 1] * inv[i]) % mod

dp = [0] * N
for i in range(N):
    f1 = (fact[N] * fact_inv[N - i] * fact_inv[i]) % mod
    f2 = (fact[N - 1] * fact_inv[N - i - 1] * fact_inv[i]) % mod
    f = (f1 * f2) % mod
    if i == 0:
        dp[i] = f
    else:
        dp[i] = (dp[i - 1] + f) % mod
print(dp[K])
