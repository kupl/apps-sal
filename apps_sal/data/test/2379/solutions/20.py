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
    temp = 0
    while day < n:
        if s[day] == 'o':
            temp += 1
            left[day] = temp
            for i in range(c):
                if day + i + 1 < n:
                    left[day + i + 1] = temp
            day += c
        else:
            left[day] = temp
        day += 1

    right = [0] * n
    day = n - 1
    temp = 0
    while 0 <= day:
        if s[day] == 'o':
            temp += 1
            right[day] = temp
            for i in range(c):
                if day - i - 1 >= 0:
                    right[day - i - 1] = temp
            day -= c
        else:
            right[day] = temp
        day -= 1

    res = []
    for i in range(n):
        if s[i] == 'o':
            if i - c - 1 < 0:
                pre = 0
            else:
                pre = left[i - c - 1]
            if i + c + 1 >= n:
                pos = 0
            else:
                pos = right[i + c + 1]
            if pre + pos == k - 1:
                res.append(i + 1)
    for i in range(len(res)):
        if i - 1 >= 0:
            l = res[i - 1]
        else:
            l = -1000000
        if i + 1 < len(res):
            r = res[i + 1]
        else:
            r = 10000000
        if res[i] - l > c and r - res[i] > c:
            print(res[i])


def __starting_point():
    main()


__starting_point()
