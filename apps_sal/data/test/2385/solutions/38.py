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
    return childs + 1, var


def dfs2(v):
    nonlocal MOD
    tNodes = 0
    tVar = 1
    for n, var in V[v].values():
        tNodes += n
        tVar *= var
        tVar %= MOD
        tVar *= invs[n]
        tVar %= MOD
    tVar *= modFacts[tNodes]
    tVar %= MOD
    dp[v] = tVar

    for e in edge[v]:
        if dp[e] == 0:
            eNodes, eVar = V[v][e]
            nVar = (tVar * invs[tNodes] * modFacts[eNodes] * modFacts[tNodes - eNodes]) % MOD
            nVar *= pow(eVar, MOD - 2, MOD)
            nVar %= MOD
            V[e][v] = (tNodes - eNodes + 1, nVar)
            dfs2(e)


N = int(input())
edge = [[] for _ in range(N)]
for s in sys.stdin.readlines():
    a, b = map(int, s.split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

modFacts, invs = prepare(N)

V = [{} for _ in range(N)]
path = [0] * N
dp = [0] * N
path[0] = 1
dfs(0)
dfs2(0)


print(*dp, sep='\n')

