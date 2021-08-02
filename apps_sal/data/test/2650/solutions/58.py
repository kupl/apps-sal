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
# from copy import deepcopy
#from collections import deque
#import numba


def binary_search(arr, operator='max'):
    _cri = {'max': max, 'min': min}
    ope = _cri[operator]
    dic = {0: arr}
    dep = 0
    while True:
        _arr = dic[dep]
        if len(_arr) == 1: break
        dic[dep + 1] = []
        for i in range(0, len(_arr), 2):
            if i == len(_arr) - 1:
                dic[dep + 1].append(_arr[i])
                continue
            dic[dep + 1].append(ope(_arr[i], _arr[i + 1]))
        dep += 1
    return _arr[0]


def eval_max(dic):
    tmp = binary_search(list(dic.keys()))
    return tmp


def run():
    N, Q = list(map(int, input().split()))
    rate = [0]
    child = [0]
    G = 2 * 10 ** 5
    group = [[] for _ in range(G + 1)]
    stocks = [[] for _ in range(G + 1)]
    for i in range(1, N + 1):
        a, b = list(map(int, sysread().split()))
        rate.append(a)
        child.append(b)
        heappush(group[b], -a)

    max_vals = []
    max_stocks = []
    for i in range(1, G + 1):
        if len(group[i]) > 0:
            heappush(max_vals, -group[i][0])

    for i in range(Q):
        c, d = list(map(int, sysread().split()))
        pre_g = child[c]
        heappush(max_stocks, -group[pre_g][0])
        heappush(stocks[pre_g], -rate[c])
        while group[pre_g] and stocks[pre_g]:
            if group[pre_g][0] == stocks[pre_g][0]:
                heappop(stocks[pre_g])
                heappop(group[pre_g])
            else:
                break
        if group[pre_g]:
            heappush(max_vals, -group[pre_g][0])

        if group[d]:
            heappush(max_stocks, -group[d][0])
        heappush(group[d], -rate[c])
        heappush(max_vals, -group[d][0])

        while max_vals and max_stocks:
            if max_vals[0] == max_stocks[0]:
                heappop(max_vals)
                heappop(max_stocks)
            else:
                break

        child[c] = d

        print((max_vals[0]))


def __starting_point():
    run()


__starting_point()
