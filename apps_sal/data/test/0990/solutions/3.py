
import numpy as np
import sys
readline = sys.stdin.readline


N = int(readline())
AB = list(list(map(int, readline().split())) for _ in range(N - 1))
M = int(readline())
UV = list(list(map(int, readline().split())) for _ in range(M))

graph = [[] for _ in range(N + 1)]
for i, (a, b) in enumerate(AB):
    graph[a].append((b, i))
    graph[b].append((a, i))


def get_path(U, V):
    INF = 100
    visited = [False] * (N + 1)
    pred = [None] * (N + 1)
    stack = [U]
    visited[U] = True
    while stack:
        v = stack.pop()
        for w, i in graph[v]:
            if visited[w]:
                continue
            visited[w] = True
            pred[w] = (v, i)
            stack.append(w)
    path = 0
    w = V
    while w != U:
        v, i = pred[w]
        w = v
        path += 1 << i
    return path


condition_path = [get_path(u, v) for u, v in UV]


def popcnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


sgn = np.where(popcnt(np.arange(1 << M)) % 2, -1, 1)
S = np.zeros(1 << M, np.int64)
for i in range(M):
    S[1 << i:1 << (i + 1)] = S[:1 << i] | condition_path[i]

n_edges = popcnt(S)

x = 1 << (N - 1 - n_edges)
answer = np.sum(x * sgn)
print(answer)
