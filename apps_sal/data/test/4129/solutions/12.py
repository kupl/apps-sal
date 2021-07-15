import sys
sys.setrecursionlimit(6000)

n, m, s = map(int, input().split())
s -= 1
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)

used = [False] * 5010
topo = []

def topo_sort(node):
    used[node] = True
    for c in g[node]:
        if not used[c]:
            topo_sort(c)
    topo.append(node)

def dfs(node):
    used[node] = True
    for c in g[node]:
        if not used[c]:
            dfs(c)

for i in range(n):
    if not used[i]:
        topo_sort(i)

topo.reverse()
for i in range(n):
    used[i] = False

dfs(s)
res = 0
for v in topo:
    if not used[v]:
        res += 1
        dfs(v)

print(res)
