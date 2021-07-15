import math as mt 
import sys,string
input=sys.stdin.readline
import random
from collections import deque,defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
t=I()
for i in range(t):
    n=input().strip()
    k=len(n)-1
    l=[]
    for i in range(len(n)):
        if(n[i]!='0'):
            l.append(int(n[i])*pow(10,k))
        k-=1
    print(len(l))
    print(*l)

