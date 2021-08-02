N = 2 * 10**5 + 3
mod = 10**9 + 7
fac = [1] * (N + 1)
for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i % mod
inv_fac = [1] * (N + 1)
inv_fac[N] = pow(fac[N], mod - 2, mod)
for i in range(N - 1, 0, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % mod


def nCr(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    return fac[n] * inv_fac[r] % mod * inv_fac[n - r] % mod


h, w, a, b = map(int, input().split())
ans = nCr(h + w - 2, h - 1)
for i in range(b):
    ans = (ans - nCr(h - a + i - 1, i) * nCr(a + w - i - 2, a - 1)) % mod
print(ans)
