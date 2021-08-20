def my_solve(n, m, graph, mask):
    if do_dfs_bool(n, graph, mask.copy()):
        c = get_cyclic(n, graph, mask)
        for (u, v) in c:
            graph[u].remove(v)
            if not do_dfs_bool(n, graph, mask.copy()):
                return 'YES'
            graph[u].append(v)
        return 'NO'
    return 'YES'


def get_cyclic(n, graph, mask):
    (c, v) = do_dfs(n, graph, mask)
    path = []
    i = 0
    begin = False
    if c:
        for u in c.keys():
            if c[u] == v:
                begin = True
                path.append((c[u], u))
            elif begin:
                path.append((c[u], u))
        tmp = list(c.keys())
        if len(tmp):
            path.append((tmp[-1], v))
    return path


def do_dfs_bool(n, graph, mask):
    colors = [0] * (n + 5)
    for u in graph.keys():
        if not u in mask.keys():
            if dfs_bool(u, graph, mask, colors):
                return True
    return False


def dfs_bool(u, graph, mask, colors):
    colors[u] = 1
    mask[u] = True
    for v in graph[u]:
        if colors[v] == 1:
            return True
        if colors[v] == 0:
            if dfs_bool(v, graph, mask, colors):
                return True
    colors[u] = 2
    return False


def do_dfs(n, graph, mask):
    colors = [0] * (n + 5)
    c = {}
    for u in graph.keys():
        if not u in mask.keys():
            c = {}
            (p, v) = dfs(u, graph, mask, c, colors)
            if p and v:
                return (p, v)


def dfs(u, graph, mask, c, colors):
    colors[u] = 1
    for v in graph[u]:
        if colors[v] == 1:
            return (c, v)
        if colors[v] == 0:
            c[v] = u
            (p, w) = dfs(v, graph, mask, c, colors)
            if w:
                return (p, w)
    colors[u] = 2
    if len(c) > 0:
        if u in c.keys():
            del c[u]
    return (c, None)


def test(n, m, edges):
    graph = {}
    mask = {}
    for (u, v) in edges:
        if u not in graph.keys():
            graph[u] = []
        graph[u].append(v)
        if v not in graph.keys():
            graph[v] = []
    return my_solve(n, m, graph, mask)


def __starting_point():
    (n, m) = [int(x) for x in input().split()]
    edges = []
    for i in range(0, m):
        (u, v) = [int(x) for x in input().split()]
        edges.append((u, v))
    print(test(n, m, edges))


__starting_point()
