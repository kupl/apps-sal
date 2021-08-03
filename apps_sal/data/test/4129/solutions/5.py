import sys

N = 5000 + 5
adj = [[] for i in range(N)]
mark = [0 for i in range(N)]
topo = []
sys.setrecursionlimit(6000)
#fin = open("999E.inp", "r")
#fou = open("999E.out", "w")
#n, m, s = map(int, fin.readline().split())
n, m, s = list(map(int, input().split()))
for i in range(m):
    #u, v = map(int, fin.readline().split())
    u, v = list(map(int, input().split()))
    adj[u].append(v)


def topoSort(u):
    mark[u] = 1
    for j in range(len(adj[u])):
        v = adj[u][j]
        if (mark[v] == 0):
            topoSort(v)
    topo.append(u)


def dfs(u):
    mark[u] = 1
    for j in range(len(adj[u])):
        v = adj[u][j]
        if (mark[v] == 0):
            dfs(v)


for i in range(1, n + 1):
    if (mark[i] == 0):
        topoSort(i)
topo.reverse()
for i in range(1, n + 1):
    mark[i] = 0
dfs(s)
res = 0
for i in range(n):
    v = topo[i]
    if (mark[v] == 0):
        res += 1
        dfs(v)
# fou.write(str(res))
print(res)
