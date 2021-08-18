from collections import deque, defaultdict


def BFS(graph, source, visited):
    n = len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while len(queue) > 0:
        u = queue.popleft()
        yield u

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


def get_components(adjacency_list, n):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            yield list(BFS(adjacency_list, i, visited))


def __starting_point():
    n, m, k = list(map(int, input().split()))
    colours = [int(x) - 1 for x in input().split()]
    adjacency_list = [[] for _ in range(n)]
    for _ in range(m):
        l, r = (int(x) - 1 for x in input().split())
        adjacency_list[l].append(r)
        adjacency_list[r].append(l)

    components = get_components(adjacency_list, n)

    changes = 0
    for component in components:
        colour_counts = defaultdict(int)
        max_count = 0
        for sock in component:
            counter = colour_counts[colours[sock]] + 1
            colour_counts[colours[sock]] = counter
            if counter > max_count:
                max_count = counter

        changes += len(component) - max_count

    print(changes)


__starting_point()
