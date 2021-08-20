from math import factorial as fact
import math
import sys
from itertools import product
import numpy as np
from collections import Counter
import datetime
from collections import deque
from bisect import bisect_left, bisect_right
import heapq


def input1():
    return int(input())


def input2():
    return list(map(int, input().split()))


def input_array():
    return list(map(int, input().split()))


(n, m) = input2()
AB = [[] for _ in range(m)]
for i in range(n):
    (a, b) = input2()
    if a - 1 < m:
        AB[a - 1].append(-b)
ans = 0
heap = []
for i in range(m):
    for b in AB[i]:
        heapq.heappush(heap, b)
    if len(heap) > 0:
        MAX = heapq.heappop(heap)
        ans += -MAX
print(ans)
