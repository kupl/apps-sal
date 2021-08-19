#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

H, W, N = map(int, input().split())

L = []
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(3):
        if a + i - 1 <= 1 or a + i - 1 >= H:
            continue
        for j in range(3):
            if b + j - 1 <= 1 or b + j - 1 >= W:
                continue
            L.append((a + i - 1, b + j - 1))
L.sort()
C = Counter(L)

ans = [0] * 10
for value in C.values():
    ans[value] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])

print('\n'.join(map(str, ans)))
