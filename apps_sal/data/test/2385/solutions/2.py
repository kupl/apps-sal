import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solve():
    MOD = 10**9 + 7

    N = int(input())
    adjL = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list(map(int, input().split()))
        a, b = a - 1, b - 1
        adjL[a].append(b)
        adjL[b].append(a)

    def getFacts(n, MOD):
        facts = [1] * (n + 1)
        for x in range(2, n + 1):
            facts[x] = (facts[x - 1] * x) % MOD
        return facts
    facts = getFacts(N, MOD)

    def getInvFacts(n, MOD):
        invFacts = [0] * (n + 1)
        invFacts[n] = pow(facts[n], MOD - 2, MOD)
        for x in reversed(list(range(n))):
            invFacts[x] = (invFacts[x + 1] * (x + 1)) % MOD
        return invFacts
    invFacts = getInvFacts(N, MOD)

    def getComb(n, k, MOD):
        if n < k:
            return 0
        return facts[n] * invFacts[k] * invFacts[n - k] % MOD

    dp = [1] * N
    sizes = [0] * N

    def dfsDP(v, vPar):
        sizes[v] = 0
        for v2 in adjL[v]:
            if v2 == vPar:
                continue
            dp[v] = dp[v] * dfsDP(v2, v) % MOD
            sizes[v] += sizes[v2]
            dp[v] = dp[v] * getComb(sizes[v], sizes[v2], MOD) % MOD
        sizes[v] += 1
        return dp[v]

    anss = [0] * N

    def dfsAns(v, vPar, resPar):
        anss[v] = dp[v] * resPar * getComb(N - 1, sizes[v] - 1, MOD) % MOD

        for v2 in adjL[v]:
            if v2 == vPar:
                continue
            coef = dp[v2] * getComb(N - 1, sizes[v2], MOD) % MOD
            dfsAns(v2, v, anss[v] * pow(coef, MOD - 2, MOD) % MOD)

    dfsDP(0, -1)
    dfsAns(0, -1, 1)

    print(('\n'.join(map(str, anss))))


solve()
