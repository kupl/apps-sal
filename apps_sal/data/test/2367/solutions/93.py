import math
p = 1000000007
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, 2 * (10**5) + 1):
    g1.append((g1[-1] * i) % p)
    inverse.append((-inverse[p % i] * (p // i)) % p)
    g2.append((g2[-1] * inverse[-1]) % p)


def cmb2(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def chwp(h, w, p):
    if h == 1 or w == 1:
        return 1
    else:
        return cmb2(h + w - 2, h - 1, p)


h, w, a, b = map(int, input().split())
ans = 0
for i in range(1, h - a + 1):
    ans = (ans + chwp(i, b, p) * chwp(h - i + 1, w - b, p)) % p
print(ans)
