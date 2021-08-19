from collections import *


def F():
    return map(int, input().split())


N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b, c) = F()
    G[a].append([a, b, c])
    G[b].append([b, a, c])
(Q, K) = F()
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
for _ in range(Q):
    (x, y) = F()
    print(D[x] + D[y])
