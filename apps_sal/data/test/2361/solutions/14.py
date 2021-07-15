from collections import *
from bisect import *
from math import *
from heapq import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    n,m,k=list(map(int,input().split()))
    x=n//k
    if(x>=m):
        print(m)
        continue
    else:
        s=x
        re=m-x
        d=ceil(re/(k-1))
        print(x-d)
    

