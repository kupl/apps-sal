n, m, k = map(int, input().split())

g = [[] for i in range(n)]
for i in range(m):
    s, v, w = map(int, input().split())
    s, v = s - 1, v - 1
    g[s].append((v, w))
    g[v].append((s, w))

if not k:
    print(-1)
    return

stores = {num - 1 for num in map(int, input().split())}
minw = float('inf')
for s in stores:
    for v, w in g[s]:
        if v not in stores:
            minw = min(minw, w)
print(minw if minw != float('inf') else -1)
