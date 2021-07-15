from collections import defaultdict, deque


N, *AB = map(int, open(0).read().split())
g = defaultdict(set)
edges = []
for a, b in zip(*[iter(AB)] * 2):
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)
    edges.append((a, b))

q = deque([0])
visited = [False] * N
visited[0] = True
used = [0] * N
colors_cnt = 1
ans = {}
while q:
    v = q.popleft()
    color = 1
    for nv in g[v]:
        if visited[nv]:
            continue
        if color == used[v]:
            color += 1
        used[nv] = color
        ans[(min(v, nv), max(v, nv))] = color
        color += 1
        q.append(nv)
        visited[nv] = True
    colors_cnt = max(colors_cnt, color - 1)
print(colors_cnt)
[print(ans[(a, b)]) for a, b in edges]


