"""input
10 3 3 4
"""
import sys
import heapq
import math
from collections import defaultdict as dd
l = [int(i) for i in input().split()]
l.sort()
if l[0] + l[-1] == l[1] + l[2] or l[0] + l[1] + l[2] == l[3]:
    print('YES')
else:
    print('NO')
