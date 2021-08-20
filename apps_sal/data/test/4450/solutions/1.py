import heapq
import sys
input = sys.stdin.readline
(n, m, k) = list(map(int, input().split()))
EDGE = [list(map(int, input().split())) for i in range(m)]
EDGE.sort(key=lambda x: x[2])
EDGE = EDGE[:k]
COST_vertex = [[] for i in range(n + 1)]
VERLIST = []
for (a, b, c) in EDGE:
    COST_vertex[a].append((b, c))
    COST_vertex[b].append((a, c))
    VERLIST.append(a)
    VERLIST.append(b)
VERLIST = list(set(VERLIST))
ANS = [-1 << 50] * k
for start in VERLIST:
    MINCOST = [1 << 50] * (n + 1)
    checking = [(0, start)]
    MINCOST[start] = 0
    j = 0
    while j < k:
        if not checking:
            break
        (cost, checktown) = heapq.heappop(checking)
        if cost >= -ANS[0]:
            break
        if MINCOST[checktown] < cost:
            continue
        if cost != 0 and checktown > start:
            heapq.heappop(ANS)
            heapq.heappush(ANS, -cost)
            j += 1
        for (to, co) in COST_vertex[checktown]:
            if MINCOST[to] > cost + co:
                MINCOST[to] = cost + co
                heapq.heappush(checking, (cost + co, to))
print(-ANS[0])
