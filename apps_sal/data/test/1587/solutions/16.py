import sys
import re
import queue
import collections
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)


sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []


def main():
    N = i_input()
    C = s_input()
    c = []
    for i in range(0, N):
        c.append(C[i])

    answer = 40000000

    tmp = 0
    for i in range(0, N):
        if(c[i] == "R"):
            tmp += 1

    answer = min(answer, tmp)

    tmp = 0
    for i in range(0, N):
        if(c[i] == "W"):
            tmp += 1

    answer = min(answer, tmp)

    whiteCount = 0
    redCount = 0
    for i in range(0, N):
        if(c[i] == "R"):
            redCount += 1
    whiteCount = N - redCount

    leftWhiteCount = 0
    rightRedCount = redCount
    for i in range(0, N):
        if(c[i] == "W"):
            leftWhiteCount += 1
        else:
            rightRedCount += -1
        answer = min(answer, max(leftWhiteCount, rightRedCount))

    print(answer)

    return


def __starting_point():
    main()


__starting_point()
