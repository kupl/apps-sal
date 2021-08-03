import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

INF = float('inf')

N, u, v = list(map(int, input().split()))
u, v = u - 1, v - 1
adjL = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    adjL[a].append(b)
    adjL[b].append(a)


def bfsMinCosts(adjList, vSt, INF):
    numV = len(adjList)
    costs = [INF] * numV
    costs[vSt] = cost = 0
    vs = [vSt]
    while vs:
        cost += 1
        v2s = []
        for v in vs:
            for v2 in adjList[v]:
                if costs[v2] == INF:
                    costs[v2] = cost
                    v2s.append(v2)
        vs = v2s
    return costs


costUs = bfsMinCosts(adjL, u, INF)
costVs = bfsMinCosts(adjL, v, INF)

ans = 0
for x in range(N):
    if costUs[x] < costVs[x]:
        if costVs[x] > ans:
            ans = costVs[x]

print((ans - 1))
