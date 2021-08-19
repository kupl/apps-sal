# inputs
n, m, ngovs = [int(x) for x in input().split()]

govs = [int(i) - 1 for i in input().split()]

# build graph
graph = [list([]) for i in range(n)]
visited = [False for i in range(n)]
for i in range(m):
    verts = tuple(int(x) - 1 for x in input().split())
    graph[verts[0]].append(verts[1])
    graph[verts[1]].append(verts[0])


# DFS
res = 0
cur_max = 0


def dfs(node):
    if not visited[node]:
        visited[node] = 1
        seen[0] += 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


for i in govs:
    seen = [0]
    dfs(i)
    res += seen[0] * (seen[0] - 1) // 2
    cur_max = max(cur_max, seen[0])

res -= cur_max * (cur_max - 1) // 2
for i in range(n):
    if not visited[i]:
        seen = [0]
        dfs(i)
        cur_max += seen[0]

res = res - m + cur_max * (cur_max - 1) // 2

print(res)
