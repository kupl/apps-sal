import sys
from collections import deque


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    n, m = map(int, sys.stdin.readline().split())
    r = [int(i) for i in sys.stdin.readline().split()]
    es = [[] for i in range(n)]

    for i in range(m):
        line = [int(j) for j in sys.stdin.readline().split()]

        for u in line[1:]:
            es[u - 1].append(i)

    Adj = [[] for i in range(m)]

    for u, v in es:
        Adj[u].append(v)
        Adj[v].append(u)

    edges = dict()

    for i, e in enumerate(es):
        e.sort()
        if tuple(e) not in edges:
            edges[tuple(e)] = r[i]
        elif edges[tuple(e)] != r[i]:
            print('NO')
            return None
        else:
            pass

    cols = [None] * m

    for u in range(m):
        if cols[u] is None:
            if not bfs(Adj, edges, cols, u):
                print('NO')
                return None
            else:
                pass

    print('YES')


def bfs(Adj, edges, cols, u):
    nxts = deque([u])
    cols[u] = 0

    while nxts:
        v = nxts.popleft()

        for w in Adj[v]:
            ed = tuple(sorted([v, w]))
            if cols[w] is None:
                if edges[ed] == 1:
                    cols[w] = cols[v]
                else:
                    cols[w] = 1 - cols[v]
                nxts.append(w)
            else:
                if edges[ed] == 1 and cols[w] != cols[v]:
                    return False
                elif edges[ed] == 0 and cols[w] == cols[v]:
                    return False

    return True


def __starting_point():
    solve()


__starting_point()
