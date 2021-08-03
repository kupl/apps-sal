from collections import deque

n, x, y = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(n - 1):
    g[i].append(i + 1)
    g[i + 1].append(i)
g[x - 1].append(y - 1)
g[y - 1].append(x - 1)


def bfs(g, n_node, start_node):
    dist = [-1] * n_node
    dist[start_node] = 0
    que = deque([start_node])

    while que:
        node = que.popleft()
        for j in g[node]:
            if dist[j] != -1:
                continue
            dist[j] = dist[node] + 1
            que.append(j)
    return dist


ans = [0] * n

for i in range(n):
    dist = bfs(g, n, i)
    for d in dist:
        ans[d] += 1

for a in ans[1:]:
    print(a // 2)
