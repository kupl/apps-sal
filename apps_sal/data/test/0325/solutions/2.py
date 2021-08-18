def validate(paths, start):
    """
    有効な経路をDFS(深さ優先探索)
    経路をsetで返す
    """

    valid_paths = {start}
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in paths:
            continue
        for w in paths[v]:
            if w in valid_paths:
                continue
            valid_paths.add(w)
            stack.append(w)
    return valid_paths


def bellman_ford(edges, num_v, start, end):
    """
    有向グラフ(負閉路有り)の最短距離

    num_v: 頂点の数(number_of_vertex)
    edges: 頂点(from, to, cost)
    """

    INF = 10**18
    dist = [INF] * num_v
    dist[start] = 0

    for _ in range(num_v):
        updated = False
        for f, t, c in edges:
            if dist[f] == INF:
                continue

            cost = dist[f] + c
            if cost < dist[t]:
                dist[t] = cost
                updated = True
        if not updated:
            break
    else:
        return -1

    return max(-dist[end], 0)


def main():
    from collections import defaultdict

    n, m, p, *tmp = list(map(int, open(0).read().split()))

    paths_rev = defaultdict(list)
    edges = []
    for a, b, c in zip(*[iter(tmp)] * 3):
        paths_rev[b - 1].append(a - 1)
        edges.append((a - 1, b - 1, p - c))

    valid_paths = validate(paths_rev, n - 1)
    edges = [
        (a, b, c)
        for a, b, c in edges
        if a in valid_paths and b in valid_paths
    ]
    res = bellman_ford(edges, n, 0, n - 1)
    print(res)


def __starting_point():
    main()


__starting_point()
