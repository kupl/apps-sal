def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math

    n, k, c = map(int, input().split())
    s = input().rstrip()
    left = [0] * n
    day = 0
    temp = 1
    while day < n:
        if s[day] == 'o':
            left[day] = temp
            temp += 1
            day += c
        day += 1

    right = [0] * n
    day = n - 1
    temp = k
    while 0 <= day:
        if s[day] == 'o':
            right[day] = temp
            temp -= 1
            day -= c
        day -= 1

    for i in range(n):
        if left[i] == right[i] and left[i] != 0:
            print(i + 1)


def __starting_point():
    main()


__starting_point()
