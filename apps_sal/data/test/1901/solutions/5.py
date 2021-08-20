def dfs(graph, start):
    (visited, stack) = (set(), [start])
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return (visited, min([prices[v] for v in visited]))


(n, m) = list(map(int, input().split()))
prices = [0] + list(map(int, input().split()))
friendship = {x: set() for x in range(1, n + 1)}
for _ in range(m):
    (x, y) = list(map(int, input().split()))
    friendship[x].add(y)
    friendship[y].add(x)
citizens = set(range(1, n + 1))
ans = 0
while citizens:
    v = citizens.pop()
    (visited, p) = dfs(friendship, v)
    citizens.difference_update(visited)
    ans += p
print(ans)
