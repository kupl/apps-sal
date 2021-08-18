n, m, k = map(int, input().split())
mod = pow(10, 9) + 7


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, n * m + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

ans = 0
for d in range(1, n):
    tmp = d * (n - d) * m**2
    tmp %= mod
    tmp *= cmb(n * m - 2, k - 2, mod)
    ans += tmp
    ans %= mod
for d in range(1, m):
    tmp = d * (m - d) * n**2
    tmp %= mod
    tmp *= cmb(n * m - 2, k - 2, mod)
    ans += tmp
    ans %= mod
print(ans)
