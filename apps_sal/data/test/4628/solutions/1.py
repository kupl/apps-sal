import heapq
import sys
input = sys.stdin.readline
(n, m, k) = list(map(int, input().split()))
EDGE = [tuple(map(int, input().split())) for i in range(m)]
E = [[] for i in range(n + 1)]
for (x, y, w) in EDGE:
    E[x].append((y, w))
    E[y].append((x, w))
ANS = 0
COST = [[1 << 30] * (n + 1) for i in range(n + 1)]
QL = [tuple(map(int, input().split())) for i in range(k)]
for x in range(1, n + 1):
    COST[x][x] = 0
    Q = [(0, x)]
    while Q:
        (cost, fr) = heapq.heappop(Q)
        if cost > COST[x][fr]:
            continue
        for (to, c) in E[fr]:
            if COST[x][to] > cost + c:
                COST[x][to] = cost + c
                heapq.heappush(Q, (COST[x][to], to))
ANS = 1 << 60
for (x, y, _) in EDGE:
    A = 0
    for (fr, to) in QL:
        A += min(COST[fr][to], COST[fr][x] + COST[to][y], COST[to][x] + COST[fr][y])
    ANS = min(ANS, A)
print(ANS)
