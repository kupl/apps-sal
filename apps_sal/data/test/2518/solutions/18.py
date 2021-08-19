def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n, a, b = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    # x回で出来るか
    def check(x):
        cnt = 0
        for i in h:
            nokori = i - b * x
            if nokori > 0:
                cnt += nokori // (a - b)
                if nokori % (a - b) != 0:
                    cnt += 1
            if cnt > x:
                return False
        return True

    l = 0
    r = 10**10
    while r - l > 1:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid

    print(r)


def __starting_point():
    main()


__starting_point()
