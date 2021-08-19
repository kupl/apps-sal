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
    return (factorials, invs)


MOD = 10 ** 9 + 7
(fact, fact_inv) = prepare(2 * 10 ** 5, MOD)
(n, m) = map(int, input().split())
if abs(n - m) > 1:
    print(0)
elif abs(n - m) == 1:
    print(fact[n] * fact[m] % MOD)
else:
    print(2 * fact[n] % MOD * fact[m] % MOD)
