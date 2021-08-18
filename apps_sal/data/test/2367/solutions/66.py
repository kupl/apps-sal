h, w, a, b = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]


for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
ans = cmb(h + w - 2, h - 1, mod)
for i in range(h - a + 1, h + 1):
    ans -= cmb(i + b - 2, i - 1, mod) * cmb(h - i + w - b - 1, w - b - 1, mod)
    ans %= mod
print(ans)
