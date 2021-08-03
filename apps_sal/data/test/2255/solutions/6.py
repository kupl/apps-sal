import queue


def __starting_point():
    n, m = list(map(int, input().split()))
    g = [set() for _ in range(n)]
    for i in range(m):
        a, b = list(map(int, input().split()))
        g[a - 1].add(b - 1)
        g[b - 1].add(a - 1)

    q = queue.PriorityQueue()
    q.put(0)

    visited = set()
    sq = []
    while len(visited) != n:
        node = q.get()
        if node not in visited:
            visited.add(node)
            sq.append(node)
        else:
            continue

        for nxt in g[node]:
            q.put(nxt)

    print(" ".join(list([str(x + 1) for x in sq])))


__starting_point()
