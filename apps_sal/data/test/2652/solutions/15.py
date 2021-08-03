from heapq import *
N = int(input())
X, Y = [], []
for n in range(N):
    x, y = map(int, input().split())
    X.append((x, n))
    Y.append((y, n))
X.sort()
Y.sort()
D = [[] for v in range(N)]
for n in range(N - 1):
    cost = X[n + 1][0] - X[n][0]
    D[X[n + 1][1]].append((cost, X[n][1]))
    D[X[n][1]].append((cost, X[n + 1][1]))
    cost = Y[n + 1][0] - Y[n][0]
    D[Y[n + 1][1]].append((cost, Y[n][1]))
    D[Y[n][1]].append((cost, Y[n + 1][1]))

visited = [0] * N
pq = []
for w, t in D[0]:
    heappush(pq, (w, t))
visited[0] = 1

ans = 0
while pq:
    w, t = heappop(pq)
    if visited[t]:
        continue
    visited[t] = 1
    ans += w
    for w, s in D[t]:
        if visited[s] == 0:
            heappush(pq, (w, s))
print(ans)
