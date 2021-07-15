from enum import Enum
from queue import Queue

import numpy as np

import collections
import bisect
import sys
import math

from scipy.sparse.csgraph import floyd_warshall

BIG_NUM = 200000000000
MOD = 1000000007
EPS = 0.000000001

def warshall_floyd(d,n):
    #d[i][j]:iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

N,M,L = list(map(int,input().split()))
d = [[float("inf") for i in range(N)] for j in range(N)]
for i in range(M):
    a,b,c = list(map(int,input().split()))
    d[a-1][b-1] = c
    d[b-1][a-1] = c
for i in range(N):
    d[i][i] = 0
d = floyd_warshall(d)
for i in range(N):
    for j in range(i,N):
        if d[i][j] <= L:
            d[i][j] = 1
            d[j][i] = 1
        else:
            d[i][j] = float("inf")
            d[j][i] = float("inf")
    d[i][i] = 1
d = floyd_warshall(d)
Q = int(input())
for q in range(Q):
    s,t = list(map(int,input().split()))
    if d[s-1][t-1] == float("inf"):
        print((-1))
    else:
        print((int(d[s-1][t-1])-1))

