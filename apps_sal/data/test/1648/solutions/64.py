from functools import lru_cache

n, k = list(map(int, input().split()))

# 2000までの階乗（MOD:10^9+7）とその逆元を計算しておく
MOD = 10**9 + 7
fact = [1, 1]
fact_inv = [1, 1]

for i in range(2, n + 1):
    fact.append(fact[i - 1] * i % MOD)
    fact_inv.append(pow(fact[i], MOD - 2, MOD))


@lru_cache(maxsize=None)
def combi(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact[n] * fact_inv[k] * fact_inv[n - k] % MOD


for i in range(1, k + 1):
    print(combi(n - k + 1, i) * combi(k - 1, i - 1) % MOD)
