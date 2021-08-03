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


def ni(): return int(sys.stdin.readline().rstrip())
def ns(): return list(map(int, sys.stdin.readline().rstrip().split()))
def na(): return list(map(int, sys.stdin.readline().rstrip().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


# ===CODE===

def main():
    n = ni()
    a = na()

    min_num = min(a)
    min_num_idx = a.index(min_num)
    max_num = max(a)
    max_num_idx = a.index(max_num)
    ans = []

    plus_flg = abs(max_num) > abs(min_num)

    if plus_flg:
        for i in range(n - 1):
            while a[i] > a[i + 1]:
                a[i + 1] += max_num
                ans.append((max_num_idx, i + 1))
            if max_num < a[i + 1]:
                max_num_idx = i + 1
                max_num = a[i + 1]

    else:
        for i in range(n - 1, 0, -1):
            while a[i - 1] > a[i]:
                a[i - 1] += min_num
                ans.append((min_num_idx, i - 1))
            if min_num > a[i - 1]:
                min_num_idx = i - 1
                min_num = a[i - 1]

    print((len(ans)))
    for a, b in ans:
        print((a + 1, b + 1))


def __starting_point():
    main()


__starting_point()
