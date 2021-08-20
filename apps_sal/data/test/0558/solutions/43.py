(n, M, K) = list(map(int, input().split()))
mod = 998244353
fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j - 1] * j % mod
inv[n] = pow(fac[n], mod - 2, mod)
for j in range(n - 1, -1, -1):
    inv[j] = inv[j + 1] * (j + 1) % mod


def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod


ans = 0
temp = M * (M - 1) ** (n - K - 1) % mod
for k in range(K + 1)[::-1]:
    ans = (ans + temp * comb(n - 1, k)) % mod
    temp = temp * (M - 1) % mod
print(ans)
