from collections import *
N = int(input())
abc = [list(map(int, input().split())) for _ in range(N - 1)]
(Q, K) = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(Q)]
G = [[] for _ in range(N + 1)]
for (a, b, c) in abc:
    G[a].append([a, b, c])
    G[b].append([b, a, c])
D = [10 ** 9 * (N + 1)] * (N + 1)
D[0] = 0
D[K] = 0
que = deque(G[K])
while que:
    (a, b, c) = que.popleft()
    if D[a] + c < D[b]:
        D[b] = D[a] + c
        for g in G[b]:
            que.append(g)
for (x, y) in xy:
    print(D[x] + D[y])
