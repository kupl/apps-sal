import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
T = [[] for _ in range(N)]
for i in range(N - 1):
    (a, b, c) = map(int, input().split())
    T[a - 1].append((b - 1, c))
    T[b - 1].append((a - 1, c))
(Q, K) = map(int, input().split())
dist = [-1] * N
dist[K - 1] = 0


def dfs(start, nown):
    to = T[start]
    for t in to:
        (next_node, c) = t
        if dist[next_node] != -1:
            continue
        nextn = nown + c
        dist[next_node] = nextn
        dfs(next_node, nextn)


dfs(K - 1, 0)
for i in range(Q):
    (x, y) = map(int, input().split())
    print(dist[x - 1] + dist[y - 1])
