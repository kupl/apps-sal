(r1, c1, r2, c2) = list(map(int, input().split()))
mod = int(1000000000.0 + 7)


def cmb(n, r, mod=mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def init_cmb(Nmax):
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, Nmax + 1):
        g1.append(g1[-1] * i % mod)
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        g2.append(g2[-1] * inverse[-1] % mod)
    return (g1, g2)


(g1, g2) = init_cmb(max(r1, r2) + max(c1, c2) + 10)


def solve(r1, c1, r2, c2):

    def f(r, c):
        return cmb(r + c, min(r, c))
    res = 0
    (r2, c2) = (r2, c2)
    res += f(r2, c2)
    res -= f(r2, c1)
    res -= f(r1, c2)
    res += f(r1, c1)
    '\n  for c in range(0,c2+1):\n    res += (c+1) * cmb(r2+c, c)\n    res %= mod\n  for c in range(0,c1):\n    res -= (c+1) * cmb(r2+c, c)\n    res %= mod\n  for r in range(0,r1):\n    res -= (r+1) * cmb(c2+r,r)\n    res %= mod\n  for r in range(0,r1):\n    res += (r+1) * cmb(c1-1+r,r)\n    res %= mod\n  '
    return res % mod


def solve2(r1, c1, r2, c2):
    res = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            res += cmb(c + r, c)
            res %= mod
    return res


print(solve(r1, c1, r2 + 1, c2 + 1))
