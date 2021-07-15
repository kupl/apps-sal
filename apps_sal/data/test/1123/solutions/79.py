import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
#from collections import defaultdict
#d = defaultdict(int)
#import fractions
#import math
#import collections
#from collections import deque
#from bisect import bisect_left
#from bisect import insort_left
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
#import itertools
#import heapq
#import numpy as np
#INF = float("inf")
#MOD = 10**9+7
MOD = 10**9+7
import math
N,K = map(int,input().split())
ans = [0]*K
for i in range(K):
    p = K-i
    a = pow(math.floor(K/p),N,MOD)
    x = 1
    while p*(x+1) <= K:
        a -= ans[p*(x+1)-1]
        x = x+1
    ans[p-1] = a%MOD
s = 0
for i in range(K):
    s += (i+1)*ans[i]
    s = s%MOD
print(s)
