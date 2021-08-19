from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = float('inf')

N, M = list(map(int, input().split()))
adjL = [[] for _ in range(3 * N)]
for _ in range(M):
    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    adjL[3 * u + 0].append(3 * v + 1)
    adjL[3 * u + 1].append(3 * v + 2)
    adjL[3 * u + 2].append(3 * v + 0)
S, T = list(map(int, input().split()))
S, T = S - 1, T - 1

# 単一始点最短経路を求める（Dijkstra法）


def Dijkstra(adjList, vSt):
    numV = len(adjList)
    numUsed = 0
    costs = [INF] * numV
    costs[vSt] = 0
    PQ = []
    heappush(PQ, (0, vSt))
    while PQ:
        cNow, vNow = heappop(PQ)
        if cNow > costs[vNow]:
            continue
        numUsed += 1
        if numUsed == numV:
            break
        for v2 in adjList[vNow]:
            c2 = cNow + 1
            if c2 < costs[v2]:
                costs[v2] = c2
                heappush(PQ, (c2, v2))
    return costs


costs = Dijkstra(adjL, 3 * S)
#print('costs:', costs)

if costs[3 * T] == INF:
    print((-1))
else:
    print((costs[3 * T] // 3))
