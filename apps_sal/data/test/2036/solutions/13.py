import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque

def r():
    return int(input())
def rm():
    return list(map(int,input().split()))
def rl():
    return list(map(int,input().split()))

n,m,x,y=rm()
print(x,y)
print(1,y)
go=True
for i in range(1,n+1):
    if go:
        for j in range(1,m+1):
            if (i==x and j==y) or (i==1 and j==y):
                continue
            print(i,j)
    else:
        for j in range(m,0,-1):
            if (i==x and j==y) or (i==1 and j==y):
                continue
            print(i,j)
    go = not go

