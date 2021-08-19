# Problem: https://atcoder.jp/contests/abc088/tasks/abc088_c
# Python 3rd Try

import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return list(map(int, sys.stdin.readline().split()))
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = (1 << 31) - 1
MINSIZE = -(1 << 31) + 1
yes = "Yes"
no = "No"


def solver(line00, line01, line02,
           line10, line11, line12,
           line20, line21, line22):

    result = no
    a0 = 0
    b0 = line00
    b1 = line01 - a0
    b2 = line02 - a0
    a1 = line10 - line00
    a2 = line20 - line00
    if ((a1 + b1) == line11) and ((a1 + b2) == line12
                                  ) and ((a2 + b1) == line21) and ((a2 + b2) == line22):
        result = yes
    return result


def __starting_point():
    line00, line01, line02 = MI()
    line10, line11, line12 = MI()
    line20, line21, line22 = MI()
    print(("{}".format(solver(line00, line01, line02,
                              line10, line11, line12,
                              line20, line21, line22))))


__starting_point()
