# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools


def blen(val):
    s = 0
    while val > 0:
        s += 1
        val >>= 1
    
    return s


def solve(N, K, X, A):
    left = [0 for _ in range(N)]
    right = [0 for _ in range(N)]
    
    for i, v in enumerate(A):
        left[i] = (left[i-1] if i-1 >= 0 else 0) | v
    for i in range(N-1, -1, -1):
        right[i] = (right[i+1] if i+1 < N else 0) | A[i]
    
    ans = 0
    for i, v in enumerate(A):
        a = left[i-1] if i-1 >= 0 else 0
        b = right[i+1] if i+1 < N else 0
        ans = max(ans, a | b | (v * X**K))
    
    return ans
    
    

N, K, X = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, K, X, A))
