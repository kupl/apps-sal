from sys import stdin
(N, M, K) = [int(x) for x in stdin.readline().rstrip().split()]
mod = 998244353
maxn = 2 * 10 ** 5 + 1
fac = [0 for _ in range(maxn)]
finv = [0 for _ in range(maxn)]
inv = [0 for _ in range(maxn)]
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, maxn):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod


def combinations(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


ans = 0
for i in range(0, K + 1):
    tmp = 1
    tmp *= M * pow(M - 1, N - i - 1, mod)
    tmp %= mod
    tmp *= combinations(N - 1, i)
    tmp %= mod
    ans += tmp
print(ans % mod)
