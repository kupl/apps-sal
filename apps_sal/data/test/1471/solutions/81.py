from collections import defaultdict
N = int(input())
edges = defaultdict(list)
for _ in range(N - 1):
    (u, v, w) = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, w))
colors = [None] * N
stack = [(0, 0)]
while stack:
    (u, c) = stack.pop()
    if colors[u] != None:
        continue
    colors[u] = c
    for (v, w) in edges[u]:
        stack.append((v, (c + w) % 2))
for u in range(N):
    print(colors[u])
