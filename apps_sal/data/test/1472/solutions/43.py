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
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        for n in g[node]:
            if dist[n] != -1:
                continue
            dist[n] = dist[node] + 1
            queue.append(n)
    return dist


ans_array = [0] * n
for i in range(n):
    dist = bfs(g, n, i)
    for d in dist:
        ans_array[d] += 1

for i in ans_array[1:]:
    print(i // 2)
