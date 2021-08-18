
def modfac(n, MOD):

    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs


def modnCr(n, r, mod, fac, inv):
    return fac[n] * inv[n - r] * inv[r] % mod


n, k = map(int, input().split())
mod = 998244353

N = n

if k >= N:
    print(0)

elif k == 0:
    ans = 1
    for i in range(1, N + 1):
        ans *= i
        ans %= mod
    print(ans)

else:

    fac, inv = modfac(n * 2 + 10, mod)

    ans = modnCr(n, k, mod, fac, inv)

    r = N - k
    p = N

    na = 0
    for i in range(r):

        now = modnCr(r, i, mod, fac, inv) * pow(r - i, p, mod)

        if i % 2 == 0:
            na += now
        else:
            na -= now
        na %= mod

    print(ans * na * 2 % mod)
