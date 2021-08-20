(n, m) = map(int, input().split())
mod = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
fact_inv = [1, 1]
inv = [0, 1]


def comb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % mod


def perm(n, r, mod):
    if r < 0 or r > n:
        return 0
    return fact[n] * fact_inv[n - r] % mod


for i in range(2, N + 1):
    fact.append(fact[-1] * i % mod)
    inv.append(-inv[mod % i] * (mod // i) % mod)
    fact_inv.append(fact_inv[-1] * inv[-1] % mod)
ans = 0
for k in range(n + 1):
    ans += comb(n, k, mod) * perm(m, k, mod) * perm(m - k, n - k, mod) ** 2 * (-1) ** k
    ans %= mod
print(ans)
