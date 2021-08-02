from collections import Counter, deque
import bisect
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")
MOD = 10**9 + 7

sys.setrecursionlimit(10**6)
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


def main():
    N = i_input()
    A = [i_input() for i in range(N)]

    L = list(set(A))
    L.sort()
    m1 = L[-1]
    cnt = A.count(m1)

    if len(L) == 1:
        m2 = m1
    else:
        m2 = L[-2]

    for i in A:
        if i == m1 and cnt == 1:
            print(m2)
        else:
            print(m1)


def __starting_point():
    main()


__starting_point()
