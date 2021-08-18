def main():
    M = int(1e12)

    n, m = list(map(int, input().split()))
    graph = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        a, b = list(map(int, input().split()))
        edges += [(a, b)]
        graph[a] |= {b}
        graph[b] |= {a}

    res = M
    for a, b in edges:
        for common in graph[a] & graph[b]:
            res = min(res, len(graph[a]) + len(graph[b]) + len(graph[common]) - 6)
    print(res if res < M else -1)


def __starting_point():
    main()


__starting_point()
