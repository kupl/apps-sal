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


(h, w, a, b) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
(facts, invs) = prepare(h + w, MOD)
ans = 0
ib = invs[b - 1]
iwb = invs[w - b - 1]
for down in range(h - a):
    left_pattern = facts[b - 1 + down] * ib * invs[down] % MOD
    right_pattern = facts[h - 1 - down + w - b - 1] * invs[h - 1 - down] * iwb % MOD
    ans = (ans + left_pattern * right_pattern) % MOD
print(ans)
