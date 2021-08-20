from math import ceil
N = int(input())
(nodes, edges) = (0, 0)
nodes = sum([i * (N - i + 1) for i in range(1, N + 1)])
for i in range(N - 1):
    (u, v) = list(map(int, input().split()))
    (u, v) = (min(u, v), max(u, v))
    edges += u * (N - v + 1)
print(nodes - edges)
