def bfs(start, end, g):
    vis = {start: -1}
    q = [start]
    found = False
    while q and not found:
        curr = q.pop(0)
        if curr == end:
            break
        for v in g[curr]:
            if v not in vis:
                vis[v] = curr
                q.append(v)
                if v == end:
                    found = True
                    break
    ans = []
    init = end
    while init != -1:
        ans.append(init)
        init = vis[init]
    return ans


n = int(input())
graph = [[] for _ in range(n)]
routers = [int(i) for i in input().split()]
for i in range(len(routers)):
    graph[routers[i] - 1].append(i + 1)
ans = bfs(0, n - 1, graph)
i = 0
j = len(ans) - 1
while i <= j:
    ans[i], ans[j] = ans[j] + 1, ans[i] + 1
    i += 1
    j -= 1
print(*ans)
