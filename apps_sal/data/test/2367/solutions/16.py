mod = 10 ** 9 + 7
h, w, a, b = map(int, input().split())
def comb(n, r):
    if n < r:return 0
    if n < 0 or r < 0:return 0
    return fa[n] * fi[r] % mod * fi[n - r] % mod
fa = [1] * (h + w + 1)
fi = [1] * (h + w + 1)
for i in range(1, h + w + 1):
    fa[i] = fa[i - 1] * i % mod
    fi[i] = pow(fa[i], mod - 2, mod)
ans = 0
for i in range(h - a):
    ans += comb(b + i - 1, b - 1) * comb(h + w - b - i - 2, w - b - 1)
    ans %= mod
print(ans % mod)
