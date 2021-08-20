def bfs(endcolor):
    color = [0] * (n + 1)
    endcolor = [0] + endcolor
    count = 0
    (visited, queue) = (set(), [1])
    while queue:
        vertex = queue.pop(0)
        if endcolor[vertex] != color[vertex]:
            color[vertex] = endcolor[vertex]
            count += 1
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(g[vertex] - visited)
            for x in g[vertex] - visited:
                color[x] = color[vertex]
    return count


n = int(input())
g = {x: set() for x in range(1, n + 2)}
i = 1
for x in map(int, input().split()):
    i += 1
    g[x].add(i)
print(bfs(list(map(int, input().split()))))
