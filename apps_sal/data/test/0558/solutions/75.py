
def main():
    MOD = 998244353

    n, m, k = list(map(int, input().split()))
    fact = [0] * 220000
    invfact = [0] * 220000

    fact[0] = 1
    for i in range(1, 220000):
        fact[i] = fact[i - 1] * i % MOD

    invfact[220000 - 1] = pow(fact[220000 - 1], MOD - 2, MOD)
    for i in range(220000 - 2, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % MOD

    def nCk(n, k):
        if k < 0 or n < k:
            return 0
        return fact[n] * invfact[k] * invfact[n - k] % MOD

    ans = 0

    for i in range(0, k + 1):
        ans += m * pow(m - 1, n - i - 1, MOD) * nCk(n - 1, i) % MOD

    print((ans % MOD))


def __starting_point():
    main()


__starting_point()
