def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n,k = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(n)]
    td.sort(reverse=True, key=lambda a: a[1])
    delicious = 0
    syurui = set()
    suteru = []
    for i in range(k):
        t, d = td[i]
        delicious += d
        if  t in syurui:
            suteru.append(d)
        else:
            syurui.add(t)
    heapify(suteru)
    neta = len(syurui)
    res = delicious + neta**2
    for i in range(k, n):
        t, d = td[i]
        if t in syurui:
            continue
        if len(suteru)==0:
            print(res)
            return
        syurui.add(t)
        delicious += d - heappop(suteru)
        neta += 1
        res = max(res, delicious+neta**2)
    print(res)

def __starting_point():
    main()
__starting_point()
