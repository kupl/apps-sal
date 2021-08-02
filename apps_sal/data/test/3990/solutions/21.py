from math import inf
from collections import Counter as cntr
n, m = map(int, input().split(' '))
road = [[1 for i in range(n)]for i in range(n)]
railway = [[0 for i in range(n)]for i in range(n)]
for i in range(m):
    u, v = map(int, input().split(' '))
    u -= 1
    v -= 1
    road[u][v] = 0
    road[v][u] = 0
    railway[u][v] = 1
    railway[v][u] = 1


def bfs(graph, source, n):
    visited = [False for i in range(n)]
    d = [inf for i in range(n)]
    q = [source]
    visited[source] = True
    d[source] = 0
    while(q):
        idx = q.pop(0)

        for i in range(n):
            if graph[idx][i] == 1 and visited[i] == False:
                visited[i] = True
                d[i] = d[idx] + 1
                q.append(i)
    return d


l1 = bfs(road, 0, n)
l2 = bfs(railway, 0, n)
ans = max(l1[-1], l2[-1])
print(-1) if ans == inf else print(ans)
