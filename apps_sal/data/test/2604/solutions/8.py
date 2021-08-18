from math import *
import itertools as it
from collections import *

EPS = 1e-9
def get_int(): return int(input().strip())
def get_string(): return input().strip()
def get_array(): return list(map(int, input().strip().split(' ')))


def print_array(a, glue=' '):
    print(glue.join(map(str, a)))


def print_grid(grid, glue=' '):
    for row in grid:
        print_array(row, glue)


def solve():
    R, D = get_array()
    n = get_int()
    r = []
    cnt = 0
    for i in range(n):
        x, y, z = get_array()
        d = sqrt(x ** 2 + y ** 2)
        if d + z <= R and d - z >= R - D:
            cnt += 1
    return cnt


ntest = 1
for _ in range(ntest):
    print(solve())
