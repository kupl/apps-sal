import sys
sys.setrecursionlimit(20000000)


def dfs(node, distance):
    for (next_node, edge_size) in G[node]:
        if ans[next_node] == -1:
            ans[next_node] = (distance + edge_size) % 2
            dfs(next_node, distance + edge_size)


N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    (u, v, w) = map(int, input().split())
    G[u - 1].append([v - 1, w])
    G[v - 1].append([u - 1, w])
ans = [-1] * N
dfs(0, 0)
print(*ans, sep='\n')
