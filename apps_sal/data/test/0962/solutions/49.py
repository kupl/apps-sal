from collections import deque
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def shorten_cycle(G, route):

    _next = {k: v for k, v in zip(route, route[1:] + route[:1])}
    v = route[0]
    while True:
        for n in G[v]:
            if n in route and n != _next[v]:
                new_route = [n]
                s = n
                while s != v:
                    s = _next[s]
                    new_route.append(s)
                _next[v] = n
                route = new_route
                v = route[0]
                break
        else:
            v = _next[v]
            if v == route[0]:
                break

    return route


def find_cycle(G, s):
    dq = deque()
    N = len(G)
    INF = float('inf')
    dist = [INF] * N
    dist[s] = 0
    parent = [-1] * N

    ans_last = None
    dq.append(s)
    while dq and ans_last is None:
        v = dq.popleft()
        d = dist[v]
        for n in G[v]:
            if dist[n] == 0:
                ans_last = v
                parent[n] = v
                break
            elif dist[n] == INF:
                dist[n] = d + 1
                parent[n] = v
                dq.append(n)

    if ans_last:
        g = ans_last
        route = [g]
        while g != s:
            g = parent[g]
            route.append(g)
        return list(reversed(route))

    return None


def main():
    N, M, *A = map(int, read().split())

    G = [[] for i in range(N + 1)]
    for a, b in zip(A[::2], A[1::2]):
        G[a].append(b)

    min_route = None
    for s in range(1, N + 1):
        route = find_cycle(G, s)
        if route:
            min_route = shorten_cycle(G, route)
            break

    if min_route:
        print(len(min_route), *min_route, sep='\n')
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
