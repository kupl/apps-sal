import sys
sys.setrecursionlimit(10**9)


def dfs(now_node, parent_node, dist):
    depth[now_node] = dist
    for next_node, w in graph[now_node]:
        if next_node == parent_node:
            continue
        dfs(next_node, now_node, dist + w)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q, k = map(int, input().split())
depth = [-1] * (n + 1)
dfs(k, 0, 0)
for _ in range(q):
    x, y = map(int, input().split())
    print(depth[x] + depth[y])
