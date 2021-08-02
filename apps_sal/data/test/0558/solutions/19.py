def main():
    N, M, K = map(int, input().split())
    MOD = 998244353

    fac = [0] * 10 ** 6
    inv = [0] * 10 ** 6
    finv = [0] * 10 ** 6

    def COM_init():
        fac[0] = 1
        fac[1] = 1
        inv[1] = 1
        finv[0] = 1
        finv[1] = 1

        for i in range(2, 2 * 10**5 + 10):
            fac[i] = fac[i - 1] * i % MOD
            inv[i] = -inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD

    def COM(n, k):
        if n < k: return 0
        if n < 0 or k < 0: return 0
        return fac[n] * (finv[n - k] * finv[k] % MOD) % MOD

    COM_init()
    ans = 0
    for i in range(K + 1):
        ans += M * pow(M - 1, N - i - 1, MOD) * COM(N - 1, i)
        ans %= MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
