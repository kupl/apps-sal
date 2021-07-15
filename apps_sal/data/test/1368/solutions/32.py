#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N,A,B = map(int, input().split())
v = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(A,B+1):
    ans = max(sum(v[:i])/i, ans)

cnt = 0
for i in range(A,B+1):
    if sum(v[:i])/i == ans:
        n = v.count(v[i-1])
        r = i-v.index(v[i-1])
        cnt += math.factorial(n)//math.factorial(r)//math.factorial(n-r)

print(ans)
print(cnt)
