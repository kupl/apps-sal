import bisect
import functools
import heapq
import itertools
import sys
import math
import random
import time
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor, itemgetter
from pprint import pprint
from types import FunctionType
from typing import List, Any
from sys import stdin

mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def inp(): return stdin.readline().rstrip()
def lmi(): return list(map(int, stdin.readline().split()))


def narray(*shape, init: Any = 0):
    if shape:
        return [narray(*shape[1:], init=init) for _ in range(shape[0])]
    if callable(init):
        return init()
    return init


def main():
    A, B = lmi()
    H, W = 100, 100
    grid = narray(H, W)
    white, black = A, B
    white -= 1
    for i in range(0, H, 4):
        for j in range(0, W, 4):
            if white == 0 and black == 0:
                break
            elif black == 0:
                if i > 0:
                    # up
                    for yd, xd in ((-1, 0), (-1, 1), (-1, 2)):
                        yy = i + yd
                        xx = j + xd
                        grid[yy][xx] = 1
                elif j > 0:
                    # left
                    for yd, xd in ((0, -1), (1, -1), (2, -1)):
                        yy = i + yd
                        xx = j + xd
                        grid[yy][xx] = 1
            elif white == 0:
                # center
                yy = i + 1
                xx = j + 1
                grid[yy][xx] = 1
            for yd, xd in ((0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)):
                yy = i + yd
                xx = j + xd
                grid[yy][xx] = 1
            white = max(0, white - 1)
            black = max(0, black - 1)

    print((100, 100))
    for line in grid:
        print((''.join('#' if c else '.' for c in line)))


def __starting_point():
    main()


__starting_point()
