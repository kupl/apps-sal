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
def ns(): return map(int, sys.stdin.readline().rstrip().split())
def na(): return list(map(int, sys.stdin.readline().rstrip().split()))
def na1(): return list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    w, b = ns()
    l = 100
    mat = [["#" for _ in range(l)] for __ in range(l)]

    if w == 1 and b == 1:
        mat[0][0] = "."

    cnt = 0
    breakflg = False
    tmp = 1 if b > 1 else 0
    flg = False
    for i in range(0, l - 3, 3):
        for j in range(0, l - 3, 3):
            if not flg:
                if cnt < w - tmp:
                    around = "#"
                    center = "."
                else:
                    flg = True
                    break

            if flg:
                if cnt < w - tmp + b - 1:
                    around = "."
                    center = "#"
                else:
                    breakflg = True
                    break

            for n in range(3):
                for m in range(3):
                    mat[i + n][j + m] = center if n == 1 and m == 1 else around
            cnt += 1
        if breakflg:
            break

    print(l, l)
    for mi in mat:
        print(*mi, sep="")


def __starting_point():
    main()


__starting_point()
