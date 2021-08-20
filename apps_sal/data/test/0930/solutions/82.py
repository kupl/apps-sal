"""
https://www.planeta.tokyo/entry/5195/
"""


def cmb(n, r, p=10 ** 9 + 7):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
n = 2 * 10 ** 5 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, n + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
(N, k) = map(int, input().split())
ans = 0
mod = 10 ** 9 + 7
for i in range(1, min(N, k) + 1):
    ans += cmb(N, i) * cmb(N - 1, i)
print(ans % mod + 1)
