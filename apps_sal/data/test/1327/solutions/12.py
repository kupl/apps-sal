'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9 + 7


def main():
    n, m = list(map(int, ipt().split()))
    pts = [[] for i in range(8)]
    for i in range(n):
        ni = [int(i) for i in ipt().split()]
        for j in range(8):
            nm = 0
            for k in range(3):
                if (j >> k) & 1:
                    nm += ni[k]
                else:
                    nm -= ni[k]
            pts[j].append(nm)

    ma = 0
    for i in range(8):
        pts[i].sort(reverse=True)
        sm = sum(pts[i][:m:])
        if ma < sm:
            ma = sm
    print(ma)
    return None


def __starting_point():
    main()


__starting_point()
