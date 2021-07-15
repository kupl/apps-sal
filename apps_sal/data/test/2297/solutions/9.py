# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/24 15:28

"""

Q = int(input())
ans = []

for i in range(Q):
    l, r = map(int, input().split())
    if l % 2 == 0 and r % 2 == 0:
        ans.append((r-l)//2 + l)
    elif l % 2 == 1 and r % 2 == 0:
        ans.append((r-l+1)//2)
    elif l % 2 == 1 and r % 2 == 1:
        ans.append(0-(r-l)//2-l)
    else:
        ans.append(0-(r-l+1)//2)

print('\n'.join(map(str, ans)))
