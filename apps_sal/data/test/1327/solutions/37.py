import sys
import math
import collections
import bisect
import copy
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline())


def ns():
    return list(map(int, sys.stdin.readline().split()))


def na():
    return list(map(int, sys.stdin.readline().split()))


def na1():
    return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    (n, m) = ns()
    res = [[] for _ in range(2 ** 3)]
    if m == 0:
        print(0)
        return
    for _ in range(n):
        a = na()
        for i in range(2 ** 3):
            tmp = 0
            for j in range(3):
                if i >> j & 1:
                    tmp += -a[j]
                else:
                    tmp += a[j]
            res[i].append(tmp)
    ans = -INF
    for resi in res:
        resi.sort(reverse=True)
        ans = max(ans, sum(resi[:m]))
    print(ans)


def __starting_point():
    main()


__starting_point()
