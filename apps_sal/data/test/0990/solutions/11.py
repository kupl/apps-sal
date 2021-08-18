
import numpy as np
import sys
readline = sys.stdin.readline

N = int(readline())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, readline().split())
    lb = 1 << i
    graph[a].append((lb, b))
    graph[b].append((lb, a))

M = int(readline())


def get_path(U, V):
    visited = 0
    q = [(U, 0)]
    while q:
        v, used = q.pop()
        if v == V:
            return used
        visited |= used
        for lb, u in graph[v]:
            if lb & visited:
                continue
            q.append((u, used | lb))


condition_path = []
for i in range(M):
    u, v = map(int, readline().split())
    condition_path.append(get_path(u, v))


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
