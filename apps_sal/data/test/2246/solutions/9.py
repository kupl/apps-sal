from collections import deque, Counter


def mean_of_ways(graph, n):
    leafs = []
    distances = [None] * n
    probabilities = [0] * n
    probabilities[0] = 1
    distances[0] = 0
    used = [False] * n
    used[0] = True
    active_vertices = deque([0])
    while active_vertices:
        where = active_vertices.popleft()
        is_leaf = True
        leafs_count = [not used[v] for v in graph[where]].count(True)
        if leafs_count > 1:
            probabilities[where] /= leafs_count
        for to in graph[where]:
            if not used[to]:
                active_vertices.append(to)
                distances[to] = distances[where] + 1
                probabilities[to] = probabilities[where]
                used[to] = True
                is_leaf = False
        if is_leaf:
            leafs.append(where)
    Mx = 0
    for i in leafs:
        Mx += probabilities[i] * distances[i]
    return Mx


def main():
    n = int(input())
    graph = [list() for i in range(n)]
    for i in range(n - 1):
        (u, v) = list(map(int, input().split()))
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    print(mean_of_ways(graph, n))


main()
