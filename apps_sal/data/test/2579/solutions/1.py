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

#====================================#


def solve():
    l, r, x, y, k = get_array()
    return 'YES' if any(l <= i * k <= r for i in range(x, y + 1)) else 'NO'


ntest = 1
# ntest = get_int()
for _ in range(ntest):
    print(solve())
