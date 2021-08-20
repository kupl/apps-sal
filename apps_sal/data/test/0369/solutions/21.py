def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    (n, m) = map(int, input().split())
    s = input().rstrip()
    s = s[::-1]
    safe = []
    for i in range(n + 1):
        if s[i] == '0':
            safe.append(i)
    res = []
    pos = 0
    while pos < n:
        pre = pos
        pos += m
        if pos >= n:
            res.append(str(n - pre))
            break
        idx = bisect_left(safe, pos)
        if safe[idx] > pos:
            pos = safe[idx - 1]
        if pre == pos:
            print(-1)
            return
        res.append(str(pos - pre))
    print(*res[::-1])


def __starting_point():
    main()


__starting_point()
