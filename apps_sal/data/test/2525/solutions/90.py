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
ri = lambda: int(input())
rs = lambda: input().strip()
rl = lambda: list(map(int, input().split()))
mod = 998244353

s = rs()
q = ri()
cnt = 0
head, tail = [], []
for i in range(q):
    qry = list(input().split())
    if len(qry) == 3:
        if int(qry[1]) % 2 ^ (cnt % 2):
            head.append(qry[2])
        else:
            tail.append(qry[2])
    else:
        cnt += 1
ans = "".join(head[::-1]) + s + "".join(tail)
print((ans if cnt % 2 == 0 else ans[::-1]))
