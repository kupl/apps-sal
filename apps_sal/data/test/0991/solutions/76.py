import collections
import heapq

INF = 10 ** 18
MAX_S = 50 * 50 + 5


def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]


class edge:
    def __init__(self, to, cost, t): self.to, self.cost, self.t = to, cost, t


def main():
    N, M, S = ZZ()
    C, D = [0] * (N + 1), [0] * (N + 1)
    E = collections.defaultdict(list)
    dist = [[INF] * (MAX_S + 1) for _ in range(N + 1)]

    for _ in range(M):
        u, v, a, b = ZZ()
        E[u].append(edge(v, a, b))
        E[v].append(edge(u, a, b))

    for i in range(1, N + 1):
        C[i], D[i] = ZZ()

    S = min(S, MAX_S)
    dist[1][S] = 0

    que = list()
    heapq.heapify(que)
    heapq.heappush(que, [dist[1][S], 1, S])

    while que:
        x, v, s = heapq.heappop(que)
        if dist[v][s] < x:
            continue

        ns = min(s + C[v], MAX_S)
        if dist[v][ns] > x + D[v]:
            dist[v][ns] = x + D[v]
            heapq.heappush(que, [x + D[v], v, ns])

        for e in E[v]:
            if s - e.cost < 0:
                continue
            if dist[e.to][s - e.cost] > x + e.t:
                dist[e.to][s - e.cost] = x + e.t
                heapq.heappush(que, [x + e.t, e.to, s - e.cost])

    for i in range(2, N + 1):
        output = INF
        for j in range(MAX_S + 1):
            output = min(output, dist[i][j])
        print(output)
    return


def __starting_point():
    main()


__starting_point()
