(n, m, k) = map(int, input().split())
mod = 10 ** 9 + 7


def combination(n, r, p):
    if n < r or r < 0:
        return 0
    r = min(n - r, r)
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % p)
        inv.append(-inv[p % i] * (p // i) % p)
        factinv.append(factinv[-1] * inv[-1] % p)
    return fact[n] * factinv[r] * factinv[n - r] % p


temp = combination(n * m - 2, k - 2, mod)
ans = 0
for d in range(1, n):
    ans += d * ((n - d) * m ** 2) * temp
for d in range(1, m):
    ans += d * ((m - d) * n ** 2) * temp
print(ans % mod)
