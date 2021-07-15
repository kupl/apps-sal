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


r1, c1, r2, c2 = list(map(int, input().split()))
MOD = 10 ** 9 + 7
facts, invs = prepare(r2 + c2 + 1, MOD)
ans = 0
for i in range(r1, r2 + 1):
    d1 = facts[i + c2 + 1] * invs[c2] % MOD
    d2 = facts[i + c1] * invs[c1 - 1] % MOD
    ans = (ans + (d1 - d2) * invs[i + 1]) % MOD
print(ans)

