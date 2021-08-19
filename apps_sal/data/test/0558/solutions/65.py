(n, m, k) = map(int, input().split())
mod = 998244353
ans = 0


def comb(n, r, mod):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, n + 1):
    fact.append(fact[-1] * i % mod)
    inv.append(-inv[mod % i] * (mod // i) % mod)
    factinv.append(factinv[-1] * inv[-1] % mod)
for i in range(k + 1):
    a = pow(m - 1, n - i - 1, mod)
    b = comb(n - 1, i, mod)
    ans += a * b % mod
ans *= m
print(ans % mod)
