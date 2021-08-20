def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        s = input().rstrip()
        (up, down) = (0, 0)
        for i in s:
            if i == ')':
                up -= 1
                if down > up:
                    down = up
            else:
                up += 1
        if up >= 0:
            a.append((down, up))
        else:
            b.append((down - up, -up))
    a.sort(key=lambda a: a[0], reverse=True)
    b.sort(key=lambda a: a[0], reverse=True)
    (left, right) = (0, 0)
    for (d, u) in a:
        if left + d < 0:
            print('No')
            break
        else:
            left += u
    else:
        for (d, u) in b:
            if right + d < 0:
                print('No')
                break
            else:
                right += u
        else:
            if left == right:
                print('Yes')
            else:
                print('No')


def __starting_point():
    main()


__starting_point()
