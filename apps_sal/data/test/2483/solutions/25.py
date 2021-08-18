import sys
import math
import collections
import bisect
import itertools


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline().rstrip())
def ns(): return list(map(int, sys.stdin.readline().rstrip().split()))
def na(): return list(map(int, sys.stdin.readline().rstrip().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


def main():
    n, c = ns()
    l = 10 ** 5
    table = [[0 for _ in range(l + 1)] for __ in range(c)]

    for _ in range(n):
        s, t, ci = ns()
        ci -= 1
        table[ci][s] += 1
        table[ci][t] -= 1

    ans = 0
    tmp = 0
    for i in range(l + 1):
        fin = 0
        for j in range(c):
            if table[j][i] > 0:
                tmp += table[j][i]
            else:
                fin += table[j][i]
        ans = max(ans, tmp)
        tmp += fin
    print(ans)


def __starting_point():
    main()


__starting_point()
