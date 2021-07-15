import sys
from collections import deque

input = sys.stdin.buffer.readline
int1 = lambda x: int(x) - 1

N, M = list(map(int, input().split()))
G = [[] for _ in range(3 * N)]
for _ in range(M):
    u, v = list(map(int1, input().split()))
    G[u * 3].append(v * 3 + 1)
    G[u * 3 + 1].append(v * 3 + 2)
    G[u * 3 + 2].append(v * 3)

S, T = list(map(int1, input().split()))
S *= 3
T *= 3

# bfs
d = deque([S])
distance = [0] * (3 * N)
while d:
    v = d.popleft()
    dist_v = distance[v]
    if v == T:
        print((dist_v // 3))
        return
    for x in G[v]:
        if not distance[x]:
            d.append(x)
            distance[x] = dist_v + 1
print((-1))

