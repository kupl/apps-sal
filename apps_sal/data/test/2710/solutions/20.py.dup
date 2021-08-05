from sys import stdin
from collections import deque


def bfs(g, el, source, dest, pre):
    q = deque()
    pre.clear()
    pre.extend([None] * len(g))
    q.append(source)
    while q:
        u = q.popleft()
        for e in g[u]:
            v, c, f = el[e][1], el[e][2], el[e][3]
            if pre[v] is None and f < c and v != source:
                pre[v] = e
                q.append(v)
        if pre[dest] is not None:
            return True
    return False


def max_flow(g, el, source, sink):
    total_flow = 0
    pre = []
    while bfs(g, el, source, sink, pre):
        e = pre[sink]
        flow = int(1e9)
        path = []
        while True:
            flow = min(flow, el[e][2] - el[e][3])
            path.append(e)
            e = pre[el[e][0]]
            if e is None:
                break
        for e in path:
            el[e][3] += flow
            el[el[e][4]][3] -= flow
        total_flow += flow
    return total_flow


def add_edge(g, el, u, v, c):
    el.append([u, v, c, 0, len(el) + 1])
    el.append([v, u, 0, 0, len(el) - 1])
    g[u].append(len(el) - 2)
    g[v].append(len(el) - 1)


def main():
    n, m = [int(_) for _ in stdin.readline().split()]
    a = [int(_) for _ in stdin.readline().split()]
    b = [int(_) for _ in stdin.readline().split()]
    g = [[] for _ in range(n * 2 + 2)]
    el = []
    source = n * 2
    sink = n * 2 + 1
    inf = int(1e9)

    for line in stdin.readlines():
        u, v = [int(_) - 1 for _ in line.split()]
        add_edge(g, el, u, v + n, inf)
        add_edge(g, el, v, u + n, inf)

    for i in range(n):
        add_edge(g, el, i, i + n, a[i])
        add_edge(g, el, source, i, a[i])
        add_edge(g, el, i + n, sink, b[i])

    if sum(a) != sum(b) or max_flow(g, el, source, sink) != sum(a):
        print("NO")
    else:
        print("YES")
        tr = [[0 for j in range(n)] for i in range(n)]
        edges = [e for e in el if e[3] > 0 and e[0] < n * 2 and e[1] < n * 2]
        for edge in edges:
            def rev_idx(u):
                return u if u < n else u - n
            tr[rev_idx(edge[0])][rev_idx(edge[1])] = edge[3]
        print('\n'.join(' '.join(str(x) for x in row) for row in tr))


def __starting_point():
    main()


__starting_point()
