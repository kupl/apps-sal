(n, m) = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
ind = 1
queue = [0]
visitedOrder = {}
visited = {}
cnt = 0
while queue:
    cur = queue[-1]
    if cur not in visited:
        visited[cur] = ind
        visitedOrder[cur] = ind
        ind += 1
    neighbours = False
    for nei in edges[cur]:
        if nei not in visited:
            neighbours = True
            queue.append(nei)
            break
    if not neighbours:
        queue.pop()
        if cur != 0:
            connected = visited[cur]
            for nei in edges[cur]:
                if nei != queue[-1]:
                    connected = min(connected, visited[nei])
            visited[cur] = connected
            if connected > visitedOrder[queue[-1]]:
                cnt += 1
print(cnt)
