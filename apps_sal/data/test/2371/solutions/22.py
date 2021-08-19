#どっちで出すか注意, rstrip注意
# 提出前に見返すこと！
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left, bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    if N >= 2:
        print(max(abs(a[-1] - W), abs(a[-1] - a[-2])))
    else:
        print(abs(a[0] - W))


def __starting_point():
    main()


__starting_point()
