def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    s = input().rstrip()
    n = len(s)
    res = 0
    for i in range(n):
        if i <= (n-1)//2:
            if s[i]=='p':
                res -= 1
        else:
            if s[i] == 'g':
                res += 1
    print(res)

def __starting_point():
    main()
__starting_point()
