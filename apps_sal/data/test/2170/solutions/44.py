MOD = 10**9 + 7

MOD_t_MAX = 5 * 10**5 + 10

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


def MOD_perm(n, r):
    rtn = 1
    for _ in range(r):
        rtn *= n
        rtn %= MOD
        n -= 1
    return rtn


def main():
    n, m = map(int, input().split())
    ans = 0
    perm = MOD_perm(m, n)
    MOD_COM_init()
    for i in range(n + 1):
        tmp = perm * MOD_COM(n, i) % MOD
        ans += (-1)**i * tmp
        ans %= MOD
        if i < n:
            perm *= inv[m - i]
            perm %= MOD
    print(ans * MOD_perm(m, n) % MOD)


def __starting_point():
    main()


__starting_point()
