# coding: utf-8
from itertools import product, accumulate, combinations, product
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def run():
    N = int(input())
    nines = [9 ** i for i in range(1, 10) if 9 ** i <= N]
    sixes = [6 ** i for i in range(1, 10) if 6 ** i <= N][::-1]
    L = len(nines)
    #print(nines, sixes)
    min_ans = INF
    for K in product(list(range(9)), repeat=L):
        #print(K, '----------------')
        ans = 0
        s = 0
        for k, x in zip(K, nines):
            if k:
                ans += k
                s += x * k
        #print(ans, s)

        if s > N:
            continue
        resid = N - s
        # print(resid)
        for six in sixes:
            # print(resid)
            tmp = resid // six
            if tmp:
                ans += tmp
                resid -= six * tmp
        #print(resid, ans)
        # if resid >= 6:
        #    print(resid)
        ans += resid
        min_ans = min(min_ans, ans)

    print(min_ans)


def __starting_point():
    run()


__starting_point()
