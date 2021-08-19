import numpy as np
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
from bisect import bisect_left
from collections import deque
import math
import fractions
from collections import Counter
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
# S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
K = int(input())
if K <= 50 and K >= 2:
    a = [K] * K
    print(K)
    print((*a))
elif K == 0:
    print((2))
    print((1, 1))
elif K == 1:
    print((2))
    print((0, 3))
else:
    x = K // 50
    y = K % 50
    a = []
    for i in range(y):
        a.append(49 + x + 1)
    for j in range(50 - y):
        a.append(49 + x - y)
    print((50))
    print((*a))
