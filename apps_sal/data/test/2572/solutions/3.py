import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(grid, h, w):
    console("----- solving ------")
    console(grid)

    lst = []

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            lst.append([
                grid[h - i - 1][w - j - 1],
                grid[h - i - 1][j],
                grid[i][w - j - 1],
                grid[i][j],
            ])

    res = 0
    for vals in lst:
        vals = sorted(vals)
        median = (vals[1] + vals[2]) // 2
        for v in vals:
            res += abs(v - median)
    return res // 4


def console(*args):
    return


for case_num in range(int(input())):

    nrows, w = list(map(int, input().split()))

    grid = []
    for _ in range(nrows):
        grid.append(list(map(int, input().split())))

    res = solve(grid, h=nrows, w=w)

    print(res)
