MOD = 10**9 + 7

N, K = list(map(int, input().split()))


def getFacts(n, MOD):
    facts = [1] * (n + 1)
    for x in range(2, n + 1):
        facts[x] = (facts[x - 1] * x) % MOD
    return facts


facts = getFacts(2 * N, MOD)


def getInvFacts(n, MOD):
    invFacts = [0] * (n + 1)
    invFacts[n] = pow(facts[n], MOD - 2, MOD)
    for x in reversed(list(range(n))):
        invFacts[x] = (invFacts[x + 1] * (x + 1)) % MOD
    return invFacts


invFacts = getInvFacts(2 * N, MOD)


def getComb(n, k, MOD):
    if n < k:
        return 0
    return facts[n] * invFacts[k] * invFacts[n - k] % MOD


ans = 0
for x in range(min(K, N - 1) + 1):
    ans += getComb(N, x, MOD) * getComb(N - 1, x, MOD)
    ans %= MOD

print(ans)
