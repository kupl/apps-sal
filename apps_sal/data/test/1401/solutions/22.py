n = int(input())
a = [0] + list(map(int, input().split()))
g = [list() for i in range(n + 1)]
for i in range(2, n + 1):
    u, v = map(int, input().split())
    g[i].append((u, v))
    g[u].append((i, v))
vis = [0] * (n + 1)
stk = [(1, 0, 0)]
while stk:
    v, min_d, dist = stk.pop()
    vis[v] = 1
    for u, c in g[v]:
        if not vis[u]:
            if dist + c - min(min_d, dist + c) <= a[u]:
                stk.append((u, min(min_d, dist + c), dist + c))
print(n - vis.count(1))
