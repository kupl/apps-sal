from collections import Counter


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def main():
    N, M = map(int, input().split())

    MOD = 10**9 + 7

    MAX_N = 5 * (10 ** 5)
    fac = [0] * MAX_N
    finv = [0] * MAX_N
    inv = [0] * MAX_N

    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, MAX_N):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = -inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    def COM(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return (fac[n] * finv[n - k] % MOD) * finv[k] % MOD

    pf = prime_factorize(M)
    pc = Counter(pf)

    ans = 1
    for _, val in pc.items():
        ans *= COM(val + N - 1, N - 1)
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
