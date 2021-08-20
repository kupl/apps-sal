(n, k) = list(map(int, input().split()))
mod = 10 ** 9 + 7
f = [1] * (n + 1)
inv = [1] * (n + 1)
for i in range(1, n + 1):
    f[i] = f[i - 1] * i % mod
inv[n] = pow(f[n], mod - 2, mod)
for i in range(n, 0, -1):
    inv[i - 1] = inv[i] * i % mod


def nCr(n, r):
    if r < 1:
        return 1
    return f[n] * inv[r] % mod * inv[n - r] % mod


ans = 0
for i in range(min(k, n - 1) + 1):
    ans = (ans + nCr(n, i) * nCr(n - 1, i)) % mod
print(ans)
