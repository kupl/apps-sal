import sys
sys.setrecursionlimit(10 ** 6)
(n, u, v) = map(int, input().split())
u -= 1
v -= 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
pre = [None] * n


def dfs(node, p_node=-1):
    for c_node in graph[node]:
        if c_node == p_node:
            continue
        pre[c_node] = node
        dfs(c_node, node)


dfs(u)
path = [v]
now = v
while now != u:
    now = pre[now]
    path.append(now)
s1 = path[len(path) // 2]
p1 = path[len(path) // 2 - 1]


def dfs2(node, depth, p_node):
    mx = depth
    for c_node in graph[node]:
        if c_node == p_node:
            continue
        mx = max(mx, dfs2(c_node, depth + 1, node))
    return mx


print(dfs2(s1, 0, p1) + len(path) // 2 - 1)
