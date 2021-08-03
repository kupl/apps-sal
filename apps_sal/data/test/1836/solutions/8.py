n, m = [int(x) for x in input().split()]
E = {i: [] for i in range(1, n + 1)}
for i in range(m):
    u, v = [int(x) for x in input().split()]
    E[v].append(u)
    E[u].append(v)
tail = {i: 0 for i in range(1, n + 1)}
tail[1] = 1
for u in range(2, n + 1):
    tail[u] = max((tail[v] for v in E[u]), default=0) + 1
print(max(tail[u] * len(E[u]) for u in range(1, n + 1)))
