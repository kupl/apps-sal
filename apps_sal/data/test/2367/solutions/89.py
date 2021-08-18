def cmb1(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


h, w, a, b = map(int, input().split())

mod = 10**9 + 7
n = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

ans = 0
for i in range(b, w):
    ans += cmb1(h - a - 1 + i, i, mod) * cmb1(a - 1 + w - 1 - i, a - 1, mod)
    ans %= mod
print(ans)
