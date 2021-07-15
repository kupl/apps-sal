# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import combinations
#import bisect# lower_bound etc
import numpy as np
def run():
    N, K, *A = list(map(int, read().split()))
    B = [a for a in A if a>0]
    C = [a for a in A if a<0]
    C_abs = [-c for c in C]
    O = A.count(0)
    B = np.array(sorted(B), dtype= np.int64)
    C = np.array(sorted(C), dtype = np.int64)
    C_abs = np.array(sorted(C_abs), dtype = np.int64)
    n_neg = len(B) * len(C)
    n_0 = O * (O - 1) // 2 + O * (len(B) + len(C))

    def find(x):
        ret = 0
        if x < 0:
            ret += np.searchsorted(C, x//B, side='right').sum()

        elif x == 0:
            ret += n_0 + n_neg
        else:
            ret += n_neg + n_0
            b_count = (B ** 2 <= x).sum()
            c_count = (C ** 2 <= x).sum()
            ret += (np.searchsorted(B, x//B, side='right').sum() - b_count) // 2

            ret += (np.searchsorted(C_abs, x//C_abs, side='right').sum() - c_count) // 2
        return ret

    high = 10 ** 18
    low = -high
    current = 0
    while high - low > 1:
        tmp = find(current)
        if tmp < K:
            low = current
        else:
            high = current

        current = (low + high) // 2

    print(high)

def __starting_point():
    run()
__starting_point()
