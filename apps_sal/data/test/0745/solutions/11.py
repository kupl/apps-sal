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


def solve(n, k):
    MOD = 998244353
    if k == 0:
        ans = 1
        for i in range(2, n + 1):
            ans = ans * i % MOD
        return ans

    if k > n - 1:
        return 0

    facts, invs = prepare(n, MOD)
    use_row = n - k
    t = 1
    ans = 0
    for r in range(use_row, 0, -1):
        ans = (ans + t * facts[use_row] * invs[r] * invs[use_row - r] * pow(r, n, MOD)) % MOD
        t *= -1
    return ans * 2 * facts[n] * invs[use_row] * invs[n - use_row] % MOD


n, k = list(map(int, input().split()))
print(solve(n, k))
