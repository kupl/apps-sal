from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    l, r, d = map(int, input().split())
    graph[l-1].append((r-1, d))
    graph[r-1].append((l-1, -d))
seen = [False]*n
dist = [None]*n
for i in range(n):
    if seen[i]:
        continue
    q = deque([i])
    dist[i] = 0
    while q:
        node = q.popleft()
        if seen[node]:
            continue
        seen[node] = True
        for c_node, d in graph[node]:
            if dist[c_node] is None:
                dist[c_node] = dist[node] + d
            elif dist[c_node] != dist[node] + d:
                print('No')
                return
            q.append(c_node)
print('Yes')
