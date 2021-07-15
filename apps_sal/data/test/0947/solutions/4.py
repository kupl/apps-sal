import math as mt
import sys,string
input=sys.stdin.readline
from collections import defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda : int(input())


t=I()
for _ in range(t):
    n=I()
    f=0
    for i in range(2,int(mt.sqrt(n))+1):
        if(n%i==0):
            f=1
            key=i
            break
    if(f):
        print(n//key,n-n//key)
    else:
        print(1,n-1)

