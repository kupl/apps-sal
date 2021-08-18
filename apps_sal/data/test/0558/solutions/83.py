def fast_pow(x, n, MOD):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


def prepare(n, MOD):

    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


MOD = 998244353
fact, fact_inv = prepare(3 * 10**5, MOD)

n, m, k = map(int, input().split())

dp = [0] * (n + 1)
ans = 0
for i in range(k + 1):
    color = fast_pow(m - 1, n - 1 - i, MOD)
    order = fact[n - 1] * fact_inv[i] % MOD * fact_inv[n - 1 - i] % MOD
    ans += m * color % MOD * order % MOD
    ans %= MOD

print(ans)
