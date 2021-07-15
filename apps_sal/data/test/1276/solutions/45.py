import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
mod = 998244353

n = ri()
s = rs()
r_li, g_li, b_li = [], [], []
for i in s:
    if i == "R":
        r_li.append(i)
    if i == "G":
        g_li.append(i)
    if i == "B":
        b_li.append(i)
ans = len(r_li) * len(g_li) * len(b_li)
cnt=0
for res in range(1, n//2 + 1):
    for i in range(0, n):
        if i+2*res<=n-1:
            if s[i] != s[i+res] and s[i+res]!=s[i+res+res] and s[i+res+res]!=s[i]:
                cnt+=1
        else:
            break

print(ans-cnt)
