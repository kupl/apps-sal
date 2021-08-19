def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    n = list(input().rstrip())
    n = [0] + n
    n = n[::-1]
    ln = len(n)
    res = 0
    a = 0
    for i in range(ln):
        s = int(n[i])
        s += a
        if 0 <= s <= 4:
            res += s
            a = 0
        elif 6 <= s:
            res += 10 - s
            a = 1
        elif int(n[i + 1]) >= 5:
            res += 10 - s
            a = 1
        else:
            res += s
            a = 0
    print(res)


def __starting_point():
    main()


__starting_point()
