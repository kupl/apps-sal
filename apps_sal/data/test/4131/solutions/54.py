from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
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
    n, m = i_map()
    l = []
    for i in range(m):
        p, y = i_map()
        l.append([i, p, y, 0])

    l.sort(key=lambda x: (x[1], x[2]))
    ken = l[0][1]
    cnt = 1

    for i in l:
        if i[1] == ken:
            i[3] = cnt
            cnt += 1
        else:
            i[3] = 1
            cnt = 2
            ken = i[1]
    l.sort(key=lambda x: x[0])

    ans = []
    for i in l:
        ans.append(str(i[1]).zfill(6) + str(i[3]).zfill(6))
    for i in ans:
        print(i)


def __starting_point():
    main()


__starting_point()
