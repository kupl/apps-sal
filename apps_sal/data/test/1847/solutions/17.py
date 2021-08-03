def main():

    import sys
    import math
    #from bisect import bisect_left as bl, bisect_right as br, insort
    from heapq import heapify, heappush, heappop
    from collections import defaultdict as dd, deque, Counter
    #from itertools import permutations,combinations
    def data(): return sys.stdin.readline().strip()
    def mdata(): return list(map(int, data().split()))
    def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
    # sys.setrecursionlimit(100000)
    INF = int(1e9)
    mod = int(1e9) + 7

    x0, y0, x1, y1 = mdata()
    n = int(data())
    d = dd(int)
    for i in range(n):
        r, a, b = mdata()
        for i in range(a, b + 1):
            d[(r, i)] = 1
    if d[(x0, y0)] == 0:
        print(-1)
        return

    dist = dd(int)
    for i in d:
        dist[i] = INF
    dist[(x0, y0)] = 0
    vis = dd(int)
    s = []
    heapify(s)
    heappush(s, (0, x0, y0))

    while len(s) != 0:
        wei, x, y = heappop(s)
        vis[(x, y)] = 1

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == j == 0:
                    continue
                if d[(x + i, y + j)] == 1:
                    if dist[(x, y)] + 1 < dist[(x + i, y + j)]:
                        dist[(x + i, y + j)] = dist[(x, y)] + 1
                        if vis[(x + i, y + j)] == 0:
                            heappush(s, (dist[(x + i, y + j)], x + i, y + j))
    if dist[x1, y1] == INF:
        print(-1)
    else:
        print(dist[x1, y1])


def __starting_point():
    main()


__starting_point()
