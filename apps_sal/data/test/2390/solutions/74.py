def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    (n, C) = map(int, input().split())
    xv = [list(map(int, input().split())) for _ in range(n)]
    xv.sort()
    (a, b) = ([], [])
    kcal = 0
    for (x, v) in xv:
        kcal += v
        a.append(kcal - x)
        b.append(kcal - 2 * x)
    xv.sort(reverse=True)
    (c, d) = ([], [])
    kcal = 0
    for (x, v) in xv:
        kcal += v
        x = C - x
        c.append(kcal - x)
        d.append(kcal - 2 * x)
    for v in [a, b, c, d]:
        for i in range(1, n):
            if v[i] < v[i - 1]:
                v[i] = v[i - 1]
    res = 0
    for i in range(n):
        res = max(res, a[i], c[i])
        if i < n - 1:
            res = max(res, b[i] + c[-(i + 2)], d[i] + a[-(i + 2)])
    print(res)


def __starting_point():
    main()


__starting_point()
