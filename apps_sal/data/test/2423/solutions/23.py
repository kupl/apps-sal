N = int(input())
pairs = [tuple(map(int, input().split())) for i in range(N - 1)]

graph = {i: list() for i in range(1, N + 1)}

for el in pairs:
    x, y = el

    graph[x].append(y)
    graph[y].append(x)

print(sum(1 for i in range(1, N + 1) if len(graph[i]) == 1))

