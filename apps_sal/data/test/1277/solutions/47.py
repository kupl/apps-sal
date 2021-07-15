from collections import deque
import sys
si = sys.stdin.readline


def BFS(g, s):
    d = 0
    dt = dict()
    visited = set()
    visited.add(s)
    Q = deque([s])

    while len(Q):
        d += 1
        Qs = len(Q)
        for _ in range(Qs):
            Qpop = Q.popleft()
            for node in g[Qpop]:
                if node not in visited:
                    Q.append(node)
                    visited.add(node)
                    dt[node] = d
    return dt


def main():
    l = [int(e) for e in si().split()]
    n, u, v = l[0], l[1], l[2]
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        l = [int(e) for e in si().split()]
        graph[l[0]].append(l[1])
        graph[l[1]].append(l[0])

    udt = BFS(graph, u)
    vdt = BFS(graph, v)
    udt[u], vdt[v] = 0, 0

    vdmax = 0
    for i in range(1, n+1):
        if (vdt[i]-udt[i]) > 0 and vdt[i] > vdmax:
            vdmax = vdt[i]
    print((vdmax-1))


def __starting_point():
    main()

__starting_point()
