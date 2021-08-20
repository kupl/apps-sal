def dfs(g, u, visited, call_stack):
    visited[u] = True
    call_stack.add(u)
    for v in g[u]:
        if v in call_stack:
            return [u, v]
        if not visited[v]:
            d = dfs(g, v, visited, call_stack)
            call_stack.discard(v)
            if d is not None:
                return [u] + d
    return None


def find_cycle(g, n):
    visited = [False] * n
    d = None
    for i in range(n):
        if not visited[i]:
            call_stack = set()
            d = dfs(g, i, visited, call_stack)
            if d is not None:
                break
    return d


def __starting_point():
    (n, m) = map(int, input().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        (u, v) = map(int, input().split())
        g[u - 1].append(v - 1)
    out = False
    c = find_cycle(g, n)
    if c:
        first_index = c.index(c[-1])
        c = c[first_index:]
        for i in range(len(c) - 1):
            if i != 0:
                g[c[i - 1]].append(c[i])
            g[c[i]].remove(c[i + 1])
            out = out or find_cycle(g, n) is None
    else:
        out = True
    print('YES' if out else 'NO')


__starting_point()
