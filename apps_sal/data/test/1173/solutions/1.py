from collections import deque

def solve():
    INF = float('inf')

    N = int(input())
    Ass = [tuple([int(x)-1 for x in input().split()]) for _ in range(N)]

    adjL = [[] for _ in range(N*N)]
    indegs = [0] * (N*N)
    for i, As in enumerate(Ass):
        x, y = i, As[0]
        if x > y:
            x, y = y, x
        vPrev = x*N + y
        for A in As[1:]:
            x, y = i, A
            if x > y:
                x, y = y, x
            v = x*N + y
            adjL[vPrev].append(v)
            indegs[v] += 1
            vPrev = v

    def getMaxCostsDAG(adjList, indegs, INF):
        numV = len(adjList)
        vs = [v for v in range(numV) if indegs[v] == 0]
        costs = [INF] * numV
        for v in vs:
            costs[v] = 0
        Q = deque(vs)
        while Q:
            vNow = Q.popleft()
            cost = costs[vNow]
            for v2 in adjList[vNow]:
                indegs[v2] -= 1
                if indegs[v2] == 0:
                    costs[v2] = cost + 1
                    Q.append(v2)
        return costs

    costs = getMaxCostsDAG(adjL, indegs, INF)

    ans = max(costs)
    if ans == INF:
        print((-1))
    else:
        print((ans+1))


solve()

