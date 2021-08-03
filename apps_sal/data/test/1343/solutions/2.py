n, m, k = list(map(int, input().split()))
g = {}

for _ in range(m):
    u, v, l = list(map(int, input().split()))
    if not (u - 1) in g:
        g[u - 1] = []
    if not (v - 1) in g:
        g[v - 1] = []

    g[u - 1].append((v - 1, l))
    g[v - 1].append((u - 1, l))

storages = [] if k == 0 else list([int(x) - 1 for x in input().split()])
isstor = [False for _ in range(n)]
for s in storages:
    isstor[s] = True

best = float('inf')
for s in storages:
    if not s in g:
        continue
    for ne in g[s]:
        if isstor[ne[0]]:
            continue
        else:
            best = min(best, ne[1])

print(-1 if best == float('inf') else best)
