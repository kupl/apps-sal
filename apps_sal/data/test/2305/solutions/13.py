import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
    N = int(input())
    Cs = [A-1 for A in map(int, input().split())]
    adjL = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = list(map(int, input().split()))
        a, b = a-1, b-1
        adjL[a].append(b)
        adjL[b].append(a)

    sizeSubtrees = [1] * N
    numVs = [0] * N
    anss = [0] * N

    def dfs(vNow, vPar, clrPar):
        clrNow = Cs[vNow]
        numVNow = numVs[clrNow]
        numVPar = numVs[clrPar]
        for v2 in adjL[vNow]:
            if v2 == vPar: continue
            dfs(v2, vNow, clrNow)
            sizeSubtrees[vNow] += sizeSubtrees[v2]
        numVs[clrNow] = numVNow + sizeSubtrees[vNow]
        if clrPar != -1:
            k = sizeSubtrees[vNow] - (numVs[clrPar]-numVPar)
            anss[clrPar] += k*(k+1)//2

    dfs(0, -1, -1)

    for clr in range(N):
        if clr == Cs[0]: continue
        k = N - numVs[clr]
        anss[clr] += k*(k+1)//2

    numAll = N*(N+1)//2
    anss = [numAll-ans for ans in anss]

    print(('\n'.join(map(str, anss))))


solve()

