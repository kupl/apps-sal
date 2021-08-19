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


def solve_sub(k, n, p, factorials, invs):
    """Number of patterns where any pair(s) of p pairs appear when n dices are rolled"""
    ret = 0
    (fp, ik) = (factorials[p], invs[k - 1])
    for q in range(1, min(p, n // 2) + 1):
        tmp1 = fp * invs[q] % MOD * invs[p - q] % MOD
        tmp2 = factorials[k + n - 2 * q - 1] * invs[n - 2 * q] % MOD * ik % MOD
        if q % 2 == 1:
            ret += tmp1 * tmp2
        else:
            ret -= tmp1 * tmp2
        ret %= MOD
    return ret


def solve(k, n):
    if k == 1:
        return [0]
    (factorials, invs) = prepare(k + n, MOD)
    all_patterns_odd = factorials[k + n - 1] * invs[n] * invs[k - 1] % MOD
    all_patterns_even0 = factorials[k + n - 2] * invs[n] * invs[k - 2] % MOD
    all_patterns_even1 = factorials[k + n - 3] * invs[n - 1] * invs[k - 2] % MOD
    buf = []
    for i in range(2, k + 2):
        pairs = i // 2 - max(0, i - k - 1)
        if i % 2 == 0:
            ans = all_patterns_even0 - solve_sub(k - 1, n, pairs - 1, factorials, invs)
            ans += all_patterns_even1 - solve_sub(k - 1, n - 1, pairs - 1, factorials, invs)
            ans %= MOD
        else:
            ans = (all_patterns_odd - solve_sub(k, n, pairs, factorials, invs)) % MOD
        buf.append(ans)
    return buf


MOD = 998244353
(k, n) = list(map(int, input().split()))
ans = solve(k, n)
print('\n'.join(map(str, ans)))
print('\n'.join(map(str, ans[-2::-1])))
