import sys
sys.setrecursionlimit(10 ** 6)


MOD = 10 ** 9 + 7


def prepare(n):
    nonlocal MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs


def dfs(v):
    nonlocal MOD
    childs = 0
    var = 1
    for e in edge[v]:
        if path[e] == 0:
            path[e] = 1
            nc, nvar = dfs(e)
            childs += nc
            V[v][e] = (nc, nvar)
            var *= nvar
            var %= MOD
            var *= invs[nc]
            var %= MOD
    var *= modFacts[childs]
    var %= MOD
    dp[v] = (childs, var)
    return childs + 1, var


def dfs2(v, pn, pVar):
    nonlocal MOD
    oNodes, oVar = dp[v]
    tNodes = pn + oNodes
    tVar = (oVar * pVar) % MOD
    tVar *= invs[oNodes] * modFacts[tNodes] * invs[pn]
    tVar %= MOD

    dp[v] = (tNodes, tVar)

    for e in list(V[v].keys()):
        eNodes, eVar = V[v][e]
        nVar = (tVar * invs[tNodes] * modFacts[eNodes] * modFacts[tNodes - eNodes]) % MOD
        nVar *= pow(eVar, MOD - 2, MOD)
        nVar %= MOD
        dfs2(e, tNodes - eNodes + 1, nVar)


N = int(input())
edge = [[] for _ in range(N)]
for s in sys.stdin.readlines():
    a, b = list(map(int, s.split()))
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

modFacts, invs = prepare(N)

V = [{} for _ in range(N)]
path = [0] * N
dp = [None] * N
path[0] = 1
dfs(0)
dfs2(0, 0, 1)


for i in range(N):
    print((dp[i][1]))

