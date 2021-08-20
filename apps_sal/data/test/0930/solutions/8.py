nmax = 3 * 10 ** 5
mod = 10 ** 9 + 7
fac = [1] * nmax
finv = [1] * nmax
inv = [1] * nmax


def ncr_pre():
    for i in range(2, nmax):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def ncr(n, r):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod


ncr_pre()
(n, k) = list(map(int, input().split()))
ans = 0
for i in range(min(n, k + 1)):
    ans += ncr(n, i) * ncr(i + n - i - 1, i)
    ans %= mod
print(ans)
