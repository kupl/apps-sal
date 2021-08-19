import os
from io import BytesIO
from itertools import product


class CYCLE(Exception):
    ...


debug_print = lambda *args: None


def solve(n, m, gs):

    def union(u, v):
        (p, q) = (find(u), find(v))
        if p == q:
            return
        if rank[p] < rank[q]:
            (p, q) = (q, p)
        if rank[p] == rank[q]:
            rank[p] += 1
        parent[q] = p

    def find(u):
        if parent[u] == u:
            return u
        else:
            p = find(parent[u])
            parent[u] = p
            return p
    rank = [0] * (n + m)
    parent = list(range(n + m))
    for (i, j) in product(range(n), range(m)):
        if gs[i][j] == '=':
            union(i, n + j)
    vertices = set(parent)
    v_sz = len(vertices)
    g = [set() for _ in range(n + m)]
    for (i, j) in product(range(n), range(m)):
        c = gs[i][j]
        (i, j) = (parent[i], parent[n + j])
        if c == '<':
            g[i].add(j)
        elif c == '>':
            g[j].add(i)
    debug_print(vertices, g)
    (NIL, VISITED, FINAL) = (0, 1, 2)
    state = [NIL] * (n + m)
    toposort_stack = []

    def visit(v):
        debug_print(v)
        if state[v] == VISITED:
            raise CYCLE
        state[v] = VISITED
        for u in g[v]:
            if state[u] != FINAL:
                visit(u)
        state[v] = FINAL
        toposort_stack.append(v)
    try:
        for v in vertices:
            if state[v] == FINAL:
                continue
            visit(v)
    except CYCLE:
        print('No')
        return
    debug_print(toposort_stack)
    layer = [1] * (n + m)
    while toposort_stack:
        v = toposort_stack.pop()
        for u in g[v]:
            layer[u] = max(layer[u], layer[v] + 1)
    print('Yes')
    out = []
    for i in range(n):
        out.append(str(layer[parent[i]]))
    print(' '.join(out))
    out = []
    for j in range(m):
        out.append(str(layer[parent[n + j]]))
    print(' '.join(out))


def solve_from_stdin():
    (n, m) = map(int, input().split())
    gs = []
    for _ in range(n):
        gs.append(input())
    solve(n, m, gs)


solve_from_stdin()
