(n, m, k) = list(map(int, input().split()))
p = 998244353


def prepare(n):
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % p)
        inv.append(-inv[p % i] * (p // i) % p)
        factinv.append(factinv[-1] * inv[-1] % p)
    return (fact, factinv)


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    return f[n] * v[r] * v[n - r] % p


(f, v) = prepare(n)
ans = 0
for i in range(k + 1):
    a = cmb(n - 1, i, p) * m * pow(m - 1, n - i - 1, p) % p
    ans += a
    ans %= p
print(ans)
