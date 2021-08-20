from math import *
import itertools as it
from collections import *
EPS = 1e-09


def get_int():
    return int(input().strip())


def get_string():
    return input().strip()


def get_array():
    return list(map(int, input().strip().split(' ')))


def print_array(a, glue=' '):
    print(glue.join(map(str, a)))


def print_grid(grid, glue=' '):
    for row in grid:
        print_array(row, glue)


def solve():
    n = get_int()
    a = get_array()
    if a[0] % 2 == 0 or a[-1] % 2 == 0:
        return 'No'
    if n % 2 == 1:
        return 'Yes'
    return 'No'


ntest = 1
for _ in range(ntest):
    print(solve())
