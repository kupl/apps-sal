from sys import stdin


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
    return (factorials, invs)


def modnCr(n, r):
    return fac[n] * inv[n - r] * inv[r] % mod


mod = 998244353
(fac, inv) = modfac(400000, mod)
(n, k) = list(map(int, stdin.readline().split()))
l = [float('inf')]
r = [float('inf')]
for i in range(n):
    (L, R) = list(map(int, stdin.readline().split()))
    l.append(L)
    r.append(R)
l.sort()
l.reverse()
r.sort()
r.reverse()
ans = 0
now = 0
for i in range(2 * n):
    if l[-1] <= r[-1]:
        now += 1
        del l[-1]
        if now >= k:
            ans += modnCr(now - 1, k - 1)
            ans %= mod
    else:
        now -= 1
        del r[-1]
print(ans % mod)
