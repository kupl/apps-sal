# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
import bisect


S = 2 * 10**5 + 5
V = collections.defaultdict(list)
for i in range(1, S+1):
    if 2*i+1 > S:
        break
    
    j = i + 1
    while j*j-i*i <= S:
        V[j*j-i*i].append((i, j))
        j += 1


N = int(input())
X = [int(x) for x in input().split()]
ans = [0] * (N+1)
xi = 0
for i in range(2, N+1, 2):
    x = X[xi]
    xi += 1
    for v in V[x]:
        if ans[i-2] < v[0]:
            ans[i-1] = v[0]
            ans[i] = v[1]
            break
            
    if ans[i-1] == 0:
        print('No')
        return
print('Yes')

print(' '.join(map(str, [ans[i]**2-ans[i-1]**2 for i in range(1, N+1)])))


