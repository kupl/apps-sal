mod = 10**9 + 7
h, w, a, b = map(int, input().split())


def comb(a, b):
    p = fac[a - b] * fac[b] % mod
    return fac[a] * pow(p, mod - 2, mod) % mod


fac = [1]
for i in range(h + w):
    fac.append(fac[-1] * (i + 1) % mod)
ans = 0
for i in range(w - b):
    p = comb(h - a - 1 + b + i, b + i) * comb(w - b - i - 2 + a, a - 1)
    ans += p % mod
    ans %= mod
print(ans)
