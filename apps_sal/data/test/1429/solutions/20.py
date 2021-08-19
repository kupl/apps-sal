# region Header
#!/usr/bin/env python3
# from typing import *

import sys
import io
import math
import collections
import decimal
import itertools
from queue import PriorityQueue
import bisect


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)
# endregion

# _INPUT = """10 AAATACCGCG
# """
# sys.stdin = io.StringIO(_INPUT)


# def solve(N: int, S: str) -> int:
def solve(N, S):
    # count_a = [0 for _ in range(N+1)]
    # count_g = [0 for _ in range(N+1)]
    # count_c = [0 for _ in range(N+1)]
    # count_t = [0 for _ in range(N+1)]
    # for i in range(1, N + 1):
    #     count_a[i] = count_a[i-1]
    #     count_g[i] = count_g[i-1]
    #     count_c[i] = count_c[i-1]
    #     count_t[i] = count_t[i-1]
    #     if S[i-1] == 'A':
    #         count_a[i] += 1
    #     elif S[i-1] == 'G':
    #         count_g[i] += 1
    #     elif S[i-1] == 'C':
    #         count_c[i] += 1
    #     elif S[i-1] == 'T':
    #         count_t[i] += 1

    # i文字目からj文字目までの（Aの数）=（Tの数）and（Cの数）=（Gの数）となる (i,j)
    n = 0
    for i in range(-1, N - 1):
        count_a = 0
        count_g = 0
        count_c = 0
        count_t = 0
        for j in range(i + 1, N):
            if S[j] == 'A':
                count_a += 1
            elif S[j] == 'G':
                count_g += 1
            elif S[j] == 'C':
                count_c += 1
            elif S[j] == 'T':
                count_t += 1
            if (count_a == count_t) and (count_c == count_g):
                n += 1

    return n


def main():
    N, S = input().split()
    N = int(N)
    a = solve(N, S)
    print(a)


def __starting_point():
    main()


__starting_point()
