import sys
sys.setrecursionlimit(10**6)
n, u, v = map(int, input().split())
u -= 1
v -= 1
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
d1 = [None]*n
d2 = [None]*n
def dfs(node, d, p_node=-1):
    for c_node in graph[node]:
        if c_node==p_node:
            continue
        d[c_node] = d[node] + 1
        dfs(c_node, d, node)
d1[u] = 0
d2[v] = 0
dfs(u, d1)
dfs(v, d2)
ans = 0
for i, j in zip(d1, d2):
    if i<j:
        ans = max(ans, j-1)
print(ans)
