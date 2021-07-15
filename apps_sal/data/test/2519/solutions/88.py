import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
import math
import itertools
#import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
mod = 998244353

'''
1 3 3 10 15
1 1.5 1.5 2.5 3 
'''

n, k = rl()
p = rl()
sum_=0
cum, ans, ser = [],[],[]
for i in range(1,2000):
    sum_+=i
    cum.append(sum_/i)
for i in p:
    ans.append(cum[i-1])
cs = [0]
for i in range(n):
    cs.append(cs[i]+ans[i])
for i in range(n+1-k):
    ser.append(cs[i+k]-cs[i])
print((max(ser)))
    

