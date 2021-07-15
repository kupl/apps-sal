import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


# ===CODE===

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
