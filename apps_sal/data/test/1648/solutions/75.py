from math import factorial


def comb(n, r):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fac[n] * fin[r] * fin[n - r] % mod


(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
fac = [1, 1]
fin = [1, 1]
inv = [0, 1]
for i in range(2, n + 1):
    fac.append(fac[-1] * i % mod)
    inv.append(pow(i, mod - 2, mod))
    fin.append(fin[-1] * inv[-1] % mod)
for i in range(1, k + 1):
    print(comb(n - k + 1, i) * comb(k - 1, i - 1) % mod)
