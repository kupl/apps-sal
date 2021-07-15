from collections import deque, defaultdict

def BFS(graph, source, visited, colours):
    # Generator which yields all vertices connected to source (includes source)
    colour_counts = defaultdict(int)
    max_count = 0
    total = 0

    n = len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while len(queue) > 0:
        u = queue.popleft()
        total += 1
        counter = colour_counts[colours[u]] + 1
        colour_counts[colours[u]] = counter
        if counter > max_count:
            max_count = counter

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return total, max_count

def get_totals_and_maxcounts(adjacency_list, n, colours):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            yield BFS(adjacency_list, i, visited, colours)

def __starting_point():
    n, m, k = list(map(int, input().split()))
    colours = [int(x) - 1 for x in input().split()]
    adjacency_list = [[] for _ in range(n)]
    for _ in range(m):
        l, r = (int(x) - 1 for x in input().split())
        adjacency_list[l].append(r)
        adjacency_list[r].append(l)


    changes = 0
    for total, max_count in get_totals_and_maxcounts(adjacency_list, n, colours):
        changes += total - max_count

    print(changes)

__starting_point()
