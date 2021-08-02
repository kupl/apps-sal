MOD = 10**9 + 7
fac = [1, 1]


def prepare(n, mod):
    for i in range(2, n + 1):
        fac.append((fac[-1] * i) % mod)


def modcmb(n, r, mod):
    if n < 0 or r < 0 or r > n:
        return 0

    return fac[n] * pow(fac[r], mod - 2, mod) * pow(fac[n - r], mod - 2, mod) % mod


def f(r, c):
    return modcmb(r + c, r, MOD)


def g(x, y):
    return ((y + 2) * modcmb(x + y + 2, x, MOD) - (x + 1)) * pow(x + 1, MOD - 2, MOD)


def main():
    prepare(2 * 10**6 + 10, MOD)
    r1, c1, r2, c2 = list(map(int, input().split()))

    ans = g(r2, c2) - g(r1 - 1, c2) - g(r2, c1 - 1) + g(r1 - 1, c1 - 1)
    ans %= MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
