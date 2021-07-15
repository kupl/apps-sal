def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    m,k = map(int, input().split())
    if m == 0:
        if k == 0:
            print(0, 0)
        else:
            print(-1)
    elif m == 1:
        if k == 0:
            print(0,0,1,1)
        else:
            print(-1)
    else:
        if k >= 2**m:
            print(-1)
        else:
            res = []
            for i in range(2**m):
                if i != 0 and i != k:
                    res.append(i)
            if k == 0:
                res = res + [0] + res[::-1] + [0]
            else:
                res = res + [0, k] + res[::-1] + [k, 0]
            print(*res)

def __starting_point():
    main()
__starting_point()
