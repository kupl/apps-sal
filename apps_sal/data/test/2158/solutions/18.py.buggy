cost = 0


def solve(u, graph, visited):
    nonlocal cost
    visited[u] = True
    visited[u] = True
    cost = 0
    explore = -1
    subcost = 0
    current = 0
    for v in graph[u]:
        if not visited[v] and graph[u][v] > subcost:
            current = max(current, solve(v, graph, visited) + graph[u][v])
    return max(current, cost)


def __starting_point():
    N = int(input().strip())
    graph = {x: {} for x in range(N)}
    visited = [False for _ in range(N + 1)]
    for i in range(N - 1):
        u, v, c = list(map(int, input().strip().split(" ")))
        graph[u][v] = c
        graph[v][u] = c
    ans = solve(0, graph, visited)
    print(ans)


__starting_point()
