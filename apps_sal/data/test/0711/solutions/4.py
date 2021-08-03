MAX = 10**6
MOD = 10**9 + 7

fac = [0] * (MAX + 1)
finv = [0] * (MAX + 1)
inv = [0] * (MAX + 1)


def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def prime_factorize(n):
    table = {}
    while n % 2 == 0:
        table[2] = table.get(2, 0) + 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            table[f] = table.get(f, 0) + 1
            n //= f
        else:
            f += 2
    if n != 1:
        table[n] = table.get(n, 0) + 1
    return table


def __starting_point():
    n, m = list(map(int, input().split()))
    comb_init()
    prime_factor = prime_factorize(m)
    res = 1
    for v in list(prime_factor.values()):
        res *= comb(v + n - 1, n - 1)
        res %= MOD
    print(res)


__starting_point()
