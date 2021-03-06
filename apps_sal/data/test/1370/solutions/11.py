import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import decimal
import queue
sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline())


def ns():
    return list(map(int, sys.stdin.readline().split()))


def na():
    return list(map(int, sys.stdin.readline().split()))


def main():
    (h, w, k) = ns()
    mat = [list(input()) for _ in range(h)]
    ans = INF
    for i in range(2 ** (h - 1)):
        cut = format(i, 'b').count('1')
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
                if mat[yi][xi] == '1':
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
