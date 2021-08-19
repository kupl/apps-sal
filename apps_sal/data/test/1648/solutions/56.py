def C(n, r, MOD):
    num = 1
    den = 1
    for i in range(r):
        num *= n - i
        num %= MOD
        den *= i + 1
        den %= MOD
    return num * pow(den, MOD - 2, MOD) % MOD


(N, K) = list(map(int, input().split()))
MOD = 1000000007
for i in range(1, K + 1):
    print(C(N - K + 1, i, MOD) * C(K - 1, i - 1, MOD) % MOD)
