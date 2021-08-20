"""
Created on Wed Sep 23 14:49:47 2020

@author: liang
"""
import numpy as np
from itertools import combinations
'\n【組み合わせ生成】\n    itertools.combinations(iterable, r)\n【総積】\n    numpy.prod(iterable)\n'
N = int(input())
d = [0] * 5
for i in range(N):
    s = input()
    if s[0] == 'M':
        d[0] += 1
    if s[0] == 'A':
        d[1] += 1
    if s[0] == 'R':
        d[2] += 1
    if s[0] == 'C':
        d[3] += 1
    if s[0] == 'H':
        d[4] += 1
ans = 0
for lis in combinations(d, 3):
    ans += np.prod(lis)
print(ans)
