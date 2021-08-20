from collections import defaultdict, deque


def bfs(g, s, c):
    visited = set()
    q = deque([s])
    while len(q) > 0:
        v = q.pop()
        visited.add(v)
        for (adj, adj_c) in g[v]:
            if adj_c == c and adj not in visited and (adj not in q):
                q.append(adj)
    return visited


def con_components(g, c):
    visited = set()
    components = []
    for s in g.keys():
        if s not in visited:
            nodes = bfs(g, s, c)
            components.append(nodes)
            visited |= nodes
    return components


def main():
    (n, m) = map(int, input().split())
    g = defaultdict(list)
    colors = set()
    for _ in range(m):
        (a, b, c) = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))
        colors.add(c)
    components = {c: con_components(g, c) for c in colors}
    q = int(input())
    for _ in range(q):
        (u, v) = map(int, input().split())
        ct = 0
        for c in colors:
            for comp in components[c]:
                if u in comp and v in comp:
                    ct += 1
        print(ct)


def __starting_point():
    main()


__starting_point()
