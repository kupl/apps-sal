def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    s = input().rstrip()
    l, r = 0, 0
    res = 0
    while r < n:
        r += 1
        if not s[l:r] in s[r:]:
            l += 1
            res = max(res, r-l)
    print(res)

def __starting_point():
    main()
__starting_point()
