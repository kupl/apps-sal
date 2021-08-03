n, k = list(map(int, input().split()))
MOD = 10**9 + 7


def prepare(n, MOD):
    facts = [1] * (n + 1)
    for i in range(1, n + 1):
        facts[i] = facts[i - 1] * i % MOD
    invs = [1] * (n + 1)
    _invs = [1] * (n + 1)
    invs[n] = pow(facts[n], MOD - 2, MOD)
    for i in range(0, n)[::-1]:
        invs[i] = invs[i + 1] * (i + 1) % MOD
    return facts, invs


ans = 0
facts, invs = prepare(n, MOD)

for i in range(1 + min(n - 1, k)):
    ans += facts[n] * invs[i] * invs[n - i] * facts[n - 1] * invs[n - i - 1] * invs[i]
    ans %= MOD

print(ans)
