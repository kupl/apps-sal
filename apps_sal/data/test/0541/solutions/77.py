import sys
import math
import collections
import bisect
import copy


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    n, m = ns()
    d = []
    for _ in range(m):
        a, b = ns()
        d.append([a - 1, b - 1])

    d.sort(key=lambda x: x[1])

    down = -1
    ans = 0
    for a, b in d:
        if down < a:
            down = b - 1
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
