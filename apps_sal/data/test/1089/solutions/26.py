# E - Cell Distance

n, m, k = list(map(int, input().split()))
mod = 10**9 + 7

difx = 0
dify = 0

for i in range(m):
    difx += (i * (m - i) * pow(n, 2, mod)) % mod

for j in range(n):
    dify += (j * (n - j) * pow(m, 2, mod)) % mod


def comb_mod(n, r, p):
    num = 1
    den = 1
    r = min(r, n - r)
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return num * pow(den, p - 2, p)


pat = comb_mod(n * m - 2, k - 2, mod)

ans = ((difx + dify) * pat) % mod

print(ans)
