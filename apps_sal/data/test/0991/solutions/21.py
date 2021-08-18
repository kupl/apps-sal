
from heapq import heappop, heappush


def solve():
    n, m, s = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = list(map(int, input().split()))
        graph[u - 1].append([v - 1, a, b])
        graph[v - 1].append([u - 1, a, b])
    ce = [[int(i) for i in input().split()] for _ in range(n)]
    maxSilver = 50 * 49
    inf = float('inf')
    ns_map = [[inf] * (maxSilver + 1) for _ in range(n)]
    q = [[0, 0, min(maxSilver, s)]]
    ns_map[0][min(maxSilver, s)] = 0
    while q:
        ti, ni, si = heappop(q)
        for g in graph[ni]:
            n2, ai, bi = g
            if si >= ai and ns_map[n2][si - ai] > ti + bi:
                ns_map[n2][si - ai] = ti + bi
                heappush(q, [ti + bi, n2, si - ai])
        ci, di = ce[ni]
        ti += di
        si = min(si + ci, maxSilver)
        if ns_map[ni][si] > ti:
            ns_map[ni][si] = ti
            heappush(q, [ti, ni, si])
    for i in range(1, n):
        print((min(ns_map[i])))


def __starting_point():
    solve()


__starting_point()
