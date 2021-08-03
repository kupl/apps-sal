MOD = 10**9 + 7


def MOD_perm(n, r):
    rtn = 1
    for _ in range(r):
        rtn *= n
        rtn %= MOD
        n -= 1
    return rtn


def MOD_inv(a):
    b = MOD
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u = u % MOD
    if u < 0:
        u += MOD
    return u


def MOD_COM2(n, r):
    return MOD_perm(n, r) * MOD_inv(MOD_perm(r, r)) % MOD


def main():
    n, m, k = map(int, input().split())
    comb = MOD_COM2(n * m - 2, k - 2)
    ans = 0
    for i in range(1, n + 1):
        U = (i - 1) * i // 2
        U *= m * m
        U *= comb
        U %= MOD
        ans += U
        ans %= MOD
    for j in range(1, m + 1):
        L = (j - 1) * j // 2
        L *= n * n
        L *= comb
        L %= MOD
        ans += L
        ans %= MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
