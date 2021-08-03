from collections import deque

N = int(input())
abc = [list(map(int, input().split())) for _ in range(N - 1)]
q, K = map(int, input().split())

graph = [[] for i in range(N + 1)]
for i, j, k in abc:
    graph[i].append((j, k))
    graph[j].append((i, k))

r = [-1 for i in range(N + 1)]
Q = deque()
Q.append(K)
r[K] = 0

while Q:
    x = Q.popleft()
    for to, dis in graph[x]:
        if r[to] == -1:
            r[to] = r[x] + dis
            Q.append(to)

for _ in range(q):
    x, y = map(int, input().split())
    print(r[x] + r[y])
