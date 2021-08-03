import sys
readline = sys.stdin.readline

MOD = 998244353


def frac(limit):
    frac = [1] * limit
    for i in range(2, limit):
        frac[i] = i * frac[i - 1] % MOD
    fraci = [None] * limit
    fraci[-1] = pow(frac[-1], MOD - 2, MOD)
    for i in range(-2, -limit - 1, -1):
        fraci[i] = fraci[i + 1] * (limit + i + 1) % MOD
    return frac, fraci


frac, fraci = frac(1341398)


def comb(a, b):
    if not a >= b >= 0:
        return 0
    return frac[a] * fraci[b] * fraci[a - b] % MOD


N, K = map(int, readline().split())

if K == 0:
    print(frac[N])
elif K >= N:
    print(0)
else:
    res = 0
    for i in range(N - K, 0, -1):
        res = (res + comb(N - K, i) * (-1)**((N - K - i) % 2) * pow(i, N, MOD)) % MOD
    print(2 * comb(N, N - K) * res % MOD)
