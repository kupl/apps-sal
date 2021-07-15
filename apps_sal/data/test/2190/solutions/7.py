# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/11/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math


def factors(val):
    wc = []
    for i in range(2, int(math.sqrt(val)) + 2):
        if i > val:
            break
        if val % i == 0:
            c = 0
            while val % i == 0:
                c += 1
                val //= i
            wc.append((i, c))
    if val > 1:
        wc.append((val, 1))
    return wc


def expand(fc, maxd, k):
    def dfs(index, mul):
        if index >= len(fc):
            return [mul]
        
        w, c = fc[index]
        d = k - (c % k) if c % k != 0 else 0
        x = []
        t = mul * (w ** d)
        while t <= maxd:
            x.extend(dfs(index + 1, t))
            d += k
            t *= w**k
        
        return x
        
    return dfs(0, 1)
    
def solve(N, K, A):
    wc = collections.defaultdict(int)
    ans = 0
    for v in A:
        fc = factors(v)
        fc = [(f, c % K) for f, c in fc if c % K != 0]
        key = '_'.join(['{}+{}'.format(f, c) for f, c in fc])
        cov = [(f, K-c) for f, c in fc]
        ckey = '_'.join(['{}+{}'.format(f, c) for f, c in cov])
        ans += wc[ckey]
        wc[key] += 1

    return ans
    
N, K = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, K, A))
