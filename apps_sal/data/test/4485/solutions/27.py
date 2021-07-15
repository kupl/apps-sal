n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

G = [[] for j in range(n + 1)]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

for b in G[1]:
    if n in G[b]:
        print('POSSIBLE')
        return
print('IMPOSSIBLE')
