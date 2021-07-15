import sys
import math
import collections
import bisect
import itertools
import decimal
import copy
import heapq

# import numpy as np

# sys.setrecursionlimit(10 ** 6)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])
flush = lambda: sys.stdout.flush()


# ===CODE===
def main():
    t = ni()

    for _ in range(t):
        x, y, k = ns()
        ans = k
        total = k + k * y - 1

        ans += -(-total // (x - 1))
        print(ans)


def __starting_point():
    main()

__starting_point()
