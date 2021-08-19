import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def solve():
    MOD = 10 ** 9 + 7
    N = int(input())
    adjL = [[] for _ in range(N)]
    for _ in range(N - 1):
        (a, b) = list(map(int, input().split()))
        (a, b) = (a - 1, b - 1)
        adjL[a].append(b)
        adjL[b].append(a)

    def getInvs(n, MOD):
        invs = [1] * (n + 1)
        for x in range(2, n + 1):
            invs[x] = -(MOD // x) * invs[MOD % x] % MOD
        return invs
    invs = getInvs(N, MOD)
    dp = [[] for _ in range(N)]
    outdegs = [0] * N
    sizes = [0] * N
    iPars = [-1] * N

    def dfsDP(v, vPar):
        outdeg = outdegs[v] = len(adjL[v])
        dp[v] = [0] * outdeg
        res = 1
        sizes[v] = 1
        for (i, v2) in enumerate(adjL[v]):
            if v2 == vPar:
                iPars[v] = i
                continue
            dp[v][i] = dfsDP(v2, v)
            res = res * dp[v][i] % MOD
            sizes[v] += sizes[v2]
        return res * invs[sizes[v]] % MOD
    anss = [0] * N

    def dfsAns(v, vPar, resPar):
        if vPar != -1:
            dp[v][iPars[v]] = resPar
        outdeg = outdegs[v]
        dpL = [1] * (outdeg + 1)
        for i in range(outdeg):
            v2 = adjL[v][i]
            dpL[i + 1] = dpL[i] * dp[v][i] % MOD
        dpR = [1] * (outdeg + 1)
        for i in reversed(list(range(outdeg))):
            v2 = adjL[v][i]
            dpR[i] = dpR[i + 1] * dp[v][i] % MOD
        anss[v] = dpL[-1] * invs[N]
        for (i, v2) in enumerate(adjL[v]):
            if v2 == vPar:
                continue
            dfsAns(v2, v, dpL[i] * dpR[i + 1] * invs[N - sizes[v2]] % MOD)
    dfsDP(0, -1)
    dfsAns(0, -1, 0)

    def getFact(n, MOD):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i % MOD
        return fact
    factN = getFact(N, MOD)
    for v in range(N):
        anss[v] = anss[v] * factN % MOD
    print('\n'.join(map(str, anss)))


solve()
