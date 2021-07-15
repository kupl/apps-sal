from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    graph[r].append((l, r, -d))
    graph[l].append((r, l, d))

max_int = 10 ** 10
point = [None for _ in range(n)]

for v in range(n):
    Q = deque()
    if point[v] is not None:
        continue
    Q.extend(graph[v])
    while Q:
        next_v, v, d = Q.popleft()
        if point[v] is None:
            point[v] = 0
        if point[next_v] is not None:
            if point[next_v] != point[v] + d:
                print('No')
                return
            else:
                continue
        point[next_v] = point[v] + d
        Q.extend(graph[next_v])
print('Yes')
