# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:49:47 2020

@author: liang
"""

"""
【組み合わせ生成】
    itertools.combinations(iterable, r)
【総積】
    numpy.prod(iterable)
"""
from itertools import combinations
import numpy as np

N = int(input())
d = [0]*5
for i in range(N):
    s = input()
    if s[0] == "M":
        d[0] += 1
    if s[0] == "A":
        d[1] += 1
    if s[0] == "R":
        d[2] += 1
    if s[0] == "C":
        d[3] += 1
    if s[0] == "H":
        d[4] += 1
    
ans = 0
for lis in combinations(d,3):
    ans += np.prod(lis)
print(ans)
