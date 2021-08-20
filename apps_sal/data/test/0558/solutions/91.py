(N, M, K) = map(int, input().split())
mod = 998244353
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fac.append(fac[-1] * i % mod)
    inv.append(mod - inv[mod % i] * (mod // i) % mod)
    finv.append(finv[-1] * inv[-1] % mod)


def comb(n, r):
    if n < r:
        return 0
    else:
        return fac[n] * (finv[r] * finv[n - r] % mod) % mod


ans = 0
for i in range(K + 1):
    ans += comb(N - 1, i) * M * pow(M - 1, N - 1 - i, mod)
    ans %= mod
print(ans)
