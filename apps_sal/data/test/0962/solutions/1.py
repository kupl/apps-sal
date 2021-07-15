import sys
sys.setrecursionlimit(10**9)

N, M = list(map(int, input().split()))
adjL = [set() for _ in range(N)]
for _ in range(M):
    A, B = list(map(int, input().split()))
    A, B = A-1, B-1
    adjL[A].add(B)

def getCycle(adjL):
    def dfs(vNow):
        if isAvails[vNow]:
            anss.append(vNow)
            return vNow
        useds[vNow] = True
        isAvails[vNow] = True
        for v2 in adjL[vNow]:
            vRet = dfs(v2)
            if vRet == vNow or vRet == numV:
                return numV
            elif vRet != -1:
                anss.append(vNow)
                return vRet
        isAvails[vNow] = False
        return -1

    numV = len(adjL)
    useds = [False] * numV
    anss = []
    for vSt in range(numV):
        isAvails = [False] * numV
        if useds[vSt]: continue
        vRet = dfs(vSt)
        if vRet == numV:
            return anss[::-1]
    return []

cycle = getCycle(adjL)

if not cycle:
    print((-1))
    return

isAvails = [False] * N
v2s = [-1] * N
for i in range(len(cycle)):
    isAvails[cycle[i]] = True
    v2s[cycle[i-1]] = cycle[i]

while True:
    adjL2 = [set() for _ in range(N)]
    a, b = -1, -1
    for v in cycle:
        for v2 in adjL[v]:
            if isAvails[v2]:
                adjL2[v].add(v2)
                if v2s[v] != v2:
                    a, b = v, v2

    if (a, b) == (-1, -1):
        print((len(cycle)))
        print(('\n'.join([str(x+1) for x in cycle])))
        break

    adjL = adjL2

    cycle = []
    isAvails = [False] * N
    v2s[a] = b
    v = a
    while not isAvails[v]:
        cycle.append(v)
        isAvails[v] = True
        v = v2s[v]

