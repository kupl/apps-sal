from collections import deque
import sys
si = sys.stdin.readline


def BFS(g, n, s):
    d = 0
    dt = [0 for _ in range(n + 1)]
    dt[s] = 0
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
    return dt[1:]


def main():
    l = [int(e) for e in si().split()]
    (n, u, v) = (l[0], l[1], l[2])
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        l = [int(e) for e in si().split()]
        graph[l[0]].append(l[1])
        graph[l[1]].append(l[0])
    udt = BFS(graph, n, u)
    vdt = BFS(graph, n, v)
    print(-1 + max([v for (u, v) in zip(udt, vdt) if u < v]))


def __starting_point():
    main()


__starting_point()
