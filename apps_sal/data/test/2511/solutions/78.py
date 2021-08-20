import sys
sys.setrecursionlimit(10 ** 6)
(n, k) = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
ans = 1
mod = 10 ** 9 + 7


def dfs(node, p_node=-1):
    if p_node == -1:
        tmp = k
        kk = k - 1
    else:
        tmp = 1
        kk = k - 2
    for c_node in graph[node]:
        if c_node == p_node:
            continue
        tmp *= dfs(c_node, node)
        tmp *= kk
        tmp %= mod
        kk -= 1
    return tmp


print(dfs(0))
