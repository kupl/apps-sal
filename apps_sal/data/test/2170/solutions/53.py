def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


def per(n, r, p):
    if r < 0 or n < r:
        return 0
    return fact[n] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 5 * pow(10, 5)
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
(n, m) = map(int, input().split())
ans = 0
for i in range(n + 1):
    ans += pow(per(m - i, n - i, p), 2) * per(m, i, p) * cmb(n, i, p) * (-1) ** i % p
ans = ans % p
print(ans)
