import numpy as np
import sys
readline = sys.stdin.readline
N = int(readline())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    (a, b) = map(int, readline().split())
    lb = 1 << i
    graph[a].append((lb, b))
    graph[b].append((lb, a))
M = int(readline())


def get_path(U, V):
    visited = 0
    q = [(U, 0)]
    while q:
        (v, used) = q.pop()
        if v == V:
            return used
        visited |= used
        for (lb, u) in graph[v]:
            if lb & visited:
                continue
            q.append((u, used | lb))


condition_path = []
for i in range(M):
    (u, v) = map(int, readline().split())
    condition_path.append(get_path(u, v))


def popcnt(n):
    c = (n & 6148914691236517205) + (n >> 1 & 6148914691236517205)
    c = (c & 3689348814741910323) + (c >> 2 & 3689348814741910323)
    c = (c & 1085102592571150095) + (c >> 4 & 1085102592571150095)
    c = (c & 71777214294589695) + (c >> 8 & 71777214294589695)
    c = (c & 281470681808895) + (c >> 16 & 281470681808895)
    c = (c & 4294967295) + (c >> 32 & 4294967295)
    return c


sgn = np.where(popcnt(np.arange(1 << M)) % 2, -1, 1)
S = np.zeros(1 << M, np.int64)
for i in range(M):
    S[1 << i:1 << i + 1] = S[:1 << i] | condition_path[i]
n_edges = popcnt(S)
x = 1 << N - 1 - n_edges
answer = np.sum(x * sgn)
print(answer)
