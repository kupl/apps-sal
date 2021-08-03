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
    n = read_int()
    h = read_int_list()
    maxh = 0
    cur = 0
    for i in h:
        if maxh < cur:
            maxh = cur
        cur = i
        if maxh >= i + 2:
            print('No')
            break
    else:
        print('Yes')


def __starting_point():
    Main()


__starting_point()
