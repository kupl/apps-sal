(n, m, k) = map(int, input().split())
mod = 10 ** 9 + 7
f = [1]
for i in range(n * m):
    f += [f[-1] * (i + 1) % mod]


def comb(a, b):
    return f[a] * pow(f[b], mod - 2, mod) * pow(f[a - b], mod - 2, mod) % mod


ans = 0
for dist in range(1, n):
    c = n - dist
    p = c * m * m % mod
    ans += p * dist
for dist in range(1, m):
    c = m - dist
    p = c * n * n % mod
    ans += p * dist
ans %= mod
print(ans * comb(n * m - 2, k - 2) % mod)
