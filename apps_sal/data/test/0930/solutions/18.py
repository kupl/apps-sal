def prepare(n, MOD):

    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


MOD = 10**9 + 7
fact, fact_inv = prepare(3 * 10**5, MOD)

n, k = map(int, input().split())

k = min(n - 1, k)

ans = 1
for i in range(1, k + 1):
    z = fact[n] * fact_inv[i] % MOD * fact_inv[n - i] % MOD
    p = fact[n - 1] * fact_inv[n - i - 1] % MOD * fact_inv[i] % MOD
    ans += z * p % MOD
    ans %= MOD
print(ans)
