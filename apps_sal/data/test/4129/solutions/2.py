from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
(n, m, s) = list(map(int, input().split()))
s = s - 1


def read_graph():
    g = defaultdict(list)
    for _ in range(m):
        (u, v) = [int(x) - 1 for x in input().split()]
        if v != s:
            g[u].append(v)
    return g


G = read_graph()
vis = defaultdict(lambda: False)
topo = []


def dfs(u):
    for v in G[u]:
        if not vis[v]:
            vis[v] = True
            dfs(v)
    topo.append(u)


for i in range(n):
    if not vis[i]:
        vis[i] = True
        dfs(i)
vis.clear()
vis[s] = True
dfs(s)
ans = 0
for i in topo[::-1]:
    if not vis[i]:
        vis[i] = True
        ans += 1
        dfs(i)
print(ans)
