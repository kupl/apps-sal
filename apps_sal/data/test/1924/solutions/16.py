MOD = 10**9 + 7
MOD_t_MAX = 2 * 10**6 + 10

fac = [None] * MOD_t_MAX
finv = [None] * MOD_t_MAX
inv = [None] * MOD_t_MAX


def MOD_COM_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MOD_t_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def MOD_COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def main():
    r1, c1, r2, c2 = map(int, input().split())
    MOD_COM_init()
    a = MOD_COM(r2 + 1 + c2 + 1, r2 + 1) - 1
    b = MOD_COM(r2 + 1 + c1, c1) - 1
    c = MOD_COM(r1 + c2 + 1, r1) - 1
    d = MOD_COM(r1 + c1, c1) - 1
    ans = a - (b + c) + d
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
