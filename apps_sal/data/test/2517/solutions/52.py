def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    inf = 10 ** 17
    (N, M, R) = map(int, input().split())
    r = list(map(int, input().split()))
    for i in range(R):
        r[i] -= 1

    def dijkstra_heap(start, edge):
        d = [inf] * N
        used = [False] * N
        d[start] = 0
        used[start] = True
        edgelist = []
        for (a, b) in edge[start]:
            heappush(edgelist, a * 10 ** 6 + b)
        while len(edgelist):
            minedge = heappop(edgelist)
            if used[minedge % 10 ** 6]:
                continue
            node = minedge % 10 ** 6
            d[node] = minedge // 10 ** 6
            used[node] = True
            for e in edge[node]:
                if not used[e[1]]:
                    heappush(edgelist, (e[0] + d[node]) * 10 ** 6 + e[1])
        return d
    edge = [[] for i in range(N)]
    for _ in range(M):
        (x, y, z) = map(int, input().split())
        edge[x - 1].append((z, y - 1))
        edge[y - 1].append((z, x - 1))
    kyori = []
    for i in r:
        kyori.append(dijkstra_heap(i, edge))
    res = inf
    for i in permutations(range(R), R):
        l = list(i)
        path = 0
        for j in range(R - 1):
            path += kyori[l[j]][r[l[j + 1]]]
        res = min(res, path)
    print(res)


def __starting_point():
    main()


__starting_point()
