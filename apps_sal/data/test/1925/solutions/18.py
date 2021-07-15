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

a,b,n = rl()
if n/b>=1:
    print(math.floor(a*(b-1)/b))
else:
    print(math.floor(a*n/b))
