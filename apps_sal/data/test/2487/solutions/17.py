# coding: utf-8
from heapq import heappop, heappush
import sys
# from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)
#from collections import OrderedDict, defaultdict
#import math
#from itertools import product, accumulate, combinations, product
# import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque
#import numba


def sum_between(a, b):
    l, r = min(a, b), max(a, b)
    return (r - l + 1) * (r + l) // 2


def run():
    N = int(input())
    n_dots = 0
    for i in range(1, N + 1):
        n_dots += (1 + i) * i // 2
    # print(n_dots)
    ans = (N - 1) * (N + 1) * N // 2
    # print(ans)
    for i in range(N - 1):
        u, v = map(int, input().split())
        l, r = min(u, v), max(u, v)
        tmp = 0
        if l > 1:
            tmp += sum_between(r - 1, r - l + 1)
        tmp += r - l
        tmp += sum_between(N - l, 1)
        # print(tmp)
        ans -= tmp

    print(n_dots - ans)

    ans = (N - 1) * N * N


def __starting_point():
    run()


__starting_point()
