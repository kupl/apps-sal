(n, m, k) = map(int, input().split())
mod = 10 ** 9 + 7
fact = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, n * m + 1):
    fact.append(fact[-1] * i % mod)
    inv.append(inv[mod % i] * (mod - mod // i) % mod)
    finv.append(finv[-1] * inv[-1] % mod)


def nCr(n, r, mod):
    if r > n:
        return 0
    else:
        return fact[n] * finv[r] * finv[n - r] % mod


ans = 0
for i in range(1, n):
    ans += nCr(n * m - 2, k - 2, mod) * i * (n - i) * m ** 2
    ans %= mod
for i in range(1, m):
    ans += nCr(n * m - 2, k - 2, mod) * i * (m - i) * n ** 2
    ans %= mod
print(ans)
