import array
import bisect
import collections
import copy
import fractions
import functools
import heapq
import itertools
import math
import random
import re
import string
import sys
import time
import os
import timeit

sys.setrecursionlimit(10000000)
inf = float('inf')


def li(): return [int(x) for x in sys.stdin.readline().split()]
def li_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def lf(): return [float(x) for x in sys.stdin.readline().split()]
def ls(): return sys.stdin.readline().split()
def int_inp(): return int(sys.stdin.readline())
def float_inp(): return float(sys.stdin.readline())
def inp(): return sys.stdin.readline().strip()
def pf(s): return print(s, flush=True)


def main():
    if os.path.exists('input.txt'):
        sys.stdin = open('input.txt', 'r')
    t = int_inp()
    ans = []
    for _ in range(t):
        n, k, d = li()
        a = li()
        x = 1000
        for i in range(n - d + 1):
            x = min(x, len(set(a[i:i + d])))
        ans.append(x)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
