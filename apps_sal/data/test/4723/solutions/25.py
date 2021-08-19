import sys
import re
import queue
import collections
import math
from decimal import *
from copy import deepcopy
from collections import Counter, deque
import heapq
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from typing import Callable
from decimal import Decimal, getcontext
# input = sys.stdin.readline
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
    S_dush = s_input()
    T = s_input()

    answer_list = []

    for i in range(0, len(S_dush) - len(T) + 1):
        flag = True
        count = 0
        for j in range(0, len(T)):
            if(S_dush[i + j] != "?" and S_dush[i + j] != T[j]):
                count = j
                flag = False
        if(flag):
            tmp = ""
            for j in range(0, len(S_dush)):
                if(S_dush[j] == "?"):
                    tmp = tmp + "a"
                else:
                    tmp = tmp + S_dush[j]
            tmp = tmp[0:i] + T + tmp[i + len(T):len(S_dush)]
            answer_list.append(tmp)

    if(len(answer_list) == 0):
        print("UNRESTORABLE")
    else:
        answer_list.sort()
        print(answer_list[0])


def __starting_point():
    main()


__starting_point()
