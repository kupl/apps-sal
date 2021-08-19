from heapq import heappush, heappop, heapify
(n, m, s) = list(map(int, input().split()))
s = min(s, 2500)
edge = [[[] for i in range(50 * 50 + 1)] for i in range(n)]
for i in range(m):
    (u, v, a, b) = list(map(int, input().split()))
    for j in range(a, 2501):
        edge[u - 1][j].append((v - 1, j - a, b))
        edge[v - 1][j].append((u - 1, j - a, b))
for i in range(n):
    (c, d) = list(map(int, input().split()))
    for j in range(2500):
        if j + c >= 2500:
            edge[i][j].append((i, 2500, d))
        elif j + c < 2500:
            edge[i][j].append((i, j + c, d))
d = [[float('inf') for i in range(50 * 50 + 1)] for i in range(n)]
d[0][s] = 0
pq = []
heappush(pq, (0, 0, s))
while len(pq):
    (_, u, g) = heappop(pq)
    for tuple in edge[u][g]:
        if d[tuple[0]][tuple[1]] > d[u][g] + tuple[2]:
            d[tuple[0]][tuple[1]] = d[u][g] + tuple[2]
            heappush(pq, [d[u][g] + tuple[2], tuple[0], tuple[1]])
for i in range(1, n):
    print(min(d[i]))
