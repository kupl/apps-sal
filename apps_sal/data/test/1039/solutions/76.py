from collections import deque


def Graph(ab):
    G = [[] for i in range(n)]
    for (a, b, c) in ab:
        G[a - 1].append([b, c])
        G[b - 1].append([a, c])
    return G


def bfs(k):
    q = deque()
    q.append((k, -1, 0))
    dis = [0] * n
    while q:
        (V, P, cnt) = q.popleft()
        for (nv, d) in G[V - 1]:
            if nv == P:
                continue
            dis[nv - 1] = cnt + d
            q.append((nv, V, cnt + d))
    return dis


n = int(input())
abc = [list(map(int, input().split())) for _ in range(n - 1)]
G = Graph(abc)
(q, k) = map(int, input().split())
dis = bfs(k)
for _ in range(q):
    (x, y) = map(int, input().split())
    print(dis[x - 1] + dis[y - 1])
