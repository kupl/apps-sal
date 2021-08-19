import sys
import math
import collections
import bisect
import itertools
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline().rstrip())


def ns():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def na():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def na1():
    return list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


def main():
    (n, a, b) = ns()
    h = [ni() for _ in range(n)]
    upper = 10 ** 9
    lower = 0
    while upper - lower > 1:
        mid = (upper + lower) // 2
        cnt = 0
        for hi in h:
            cnt += int(math.ceil(max(0, hi - b * mid) / (a - b)))
        if cnt <= mid:
            upper = mid
        else:
            lower = mid
    print(upper)


def __starting_point():
    main()


__starting_point()
