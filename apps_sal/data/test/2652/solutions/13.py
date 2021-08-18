
import heapq as hq
import sys
readline = sys.stdin.readline

N = int(readline())
point = [None] * N
for i in range(N):
    point[i] = list(map(int, readline().split())) + [i]

X = sorted(point, key=lambda x: x[0])
Y = sorted(point, key=lambda x: x[1])

G = [[] for i in range(N)]

for i in range(len(X) - 1):
    x1, y1, ind_1 = X[i]
    x2, y2, ind_2 = X[i + 1]
    G[ind_1].append([ind_2, min(abs(x1 - x2), abs(y1 - y2))])
    G[ind_2].append([ind_1, min(abs(x1 - x2), abs(y1 - y2))])

for i in range(len(Y) - 1):
    x1, y1, ind_1 = Y[i]
    x2, y2, ind_2 = Y[i + 1]
    G[ind_1].append([ind_2, min(abs(x1 - x2), abs(y1 - y2))])
    G[ind_2].append([ind_1, min(abs(x1 - x2), abs(y1 - y2))])


q = [(0, 0)]
hq.heapify(q)
visited = set()

ans = 0
while q:
    cost, v = hq.heappop(q)
    if v in visited:
        continue
    visited.add(v)
    ans += cost
    for child in G[v]:
        if child[0] in visited:
            continue
        hq.heappush(q, (child[1], child[0]))

print(ans)
