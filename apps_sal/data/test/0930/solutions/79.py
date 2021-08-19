(n, k) = list(map(int, input().split()))
mod = 10 ** 9 + 7


def prepare():
    fact = []
    f = 1
    for m in range(1, n):
        f *= m
        f %= mod
    fact.append(f)
    f *= n
    f %= mod
    fact.append(f)
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        inv.append(-inv[mod % i] * (mod // i) % mod)
        factinv.append(factinv[-1] * inv[-1] % mod)
    return (fact, factinv)


def cmb(a, r, p):
    if r < 0 or n < r:
        return 0
    if a == 1:
        return f[a] * v[r] * v[n - r] % mod
    else:
        return f[a] * v[r] * v[n - r - 1] % mod


(f, v) = prepare()
ans = 1
for i in range(1, min(k + 1, n)):
    ans += cmb(0, i, mod) * cmb(1, i, mod)
    ans %= mod
print(ans)
