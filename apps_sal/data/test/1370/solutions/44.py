import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    h, w, k = ns()
    mat = [list(input()) for _ in range(h)]

    if h == 1:
        tmp = max(0, mat[0].count("1") - 1)
        print((tmp // k))
        return

    ans = INF
    for i in range(2 ** (h - 1)):
        cut = format(i, "b").count("1")
        row = cut + 1

        cnt = [0 for _ in range(row)]

        idx_dic = dict()
        tmp_idx = 0
        for j in range(h):
            idx_dic[j] = tmp_idx
            if i >> j & 1:
                tmp_idx += 1

        tmp_ans = cut
        xi = 0
        brkflg = True
        while xi < w:
            yi = 0
            prev_brkflg = brkflg
            brkflg = False
            while yi < h:
                if mat[yi][xi] == "1":
                    cnt[idx_dic[yi]] += 1
                    if cnt[idx_dic[yi]] > k:
                        cnt = [0 for _ in range(row)]
                        xi -= 1
                        brkflg = True
                        tmp_ans += 1
                        break

                yi += 1
            if brkflg and prev_brkflg:
                tmp_ans = INF
                break
            xi += 1
        ans = min(ans, tmp_ans)

    print(ans)


def __starting_point():
    main()

__starting_point()
