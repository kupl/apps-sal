import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


def Main():
    a, b = read_ints()
    print(100, 100)
    grid = [['#'] * 100 for _ in range(50)] + [['.'] * 100 for _ in range(50)]
    for i in range(~-a):
        x, y = divmod(i, 49)
        grid[x * 2 + 1][y * 2 + 1] = '.'
    for i in range(~-b):
        x, y = divmod(i, 49)
        grid[x * 2 + 51][y * 2 + 1] = '#'
    print(*[''.join(g) for g in grid], sep='\n')


def __starting_point():
    Main()


__starting_point()
