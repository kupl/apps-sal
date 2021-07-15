import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import bisect_right
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
from copy import deepcopy
from decimal import Decimal
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
H,W,D = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(H)]
table = [[-1,-1] for _ in range(H*W+1)]
for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a > D:
            table[a-D][0] = i
            table[a-D][1] = j
magic = [0]*(H*W+1)
for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a <= H*W-D:
            magic[a] = abs(i-table[a][0])+abs(j-table[a][1])
for i in range(D+1,H*W+1):
    magic[i] += magic[i-D]
Q = int(input())
ans = 0
for i in range(Q):
    L,R = list(map(int,input().split()))
    if L == R:
        print((0))
    else:
        if L <= D:
            print((magic[R-D]))
        else:
            print((magic[R-D]-magic[L-D]))




