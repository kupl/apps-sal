#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,K = map(int, input().split())
L = [tuple(map(int, input().split())) for i in range(N)]
L.sort()

ans = 10**20

for lx in range(N):
    for rx in range(lx+1,N+1):
        L2 = L[lx:rx]
        L2 = sorted(L2, key=lambda x:x[1])
        for ly in range(len(L2)):
            L3 = L2[ly:ly+K]
            if len(L3) >= K:
                ans = min(ans, (L[rx-1][0]-L[lx][0])*(L3[-1][1]-L3[0][1]))

print(ans)
