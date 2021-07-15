H, W, A, B = [int(_) for _ in input().split()]
mod = 10 ** 9 + 7
f = [1] * (3 * 10 ** 6 + 10)
for i in range(1, 3 * 10 ** 6 + 10):
    f[i] = i * f[i - 1] % mod
fi = {}


def comb(n, r):
    if r not in fi:
        fi[r] = pow(f[r], mod - 2, mod)
    if n - r not in fi:
        fi[n - r] = pow(f[n - r], mod - 2, mod)
    return (f[n] * fi[r] * fi[n - r]) % mod


ans = 0
for x in range(H - A):
    ans += comb(B - 1 + x, x) * comb(H - x - 2 + W - B, W - B - 1)
    ans %= mod
print(ans)

