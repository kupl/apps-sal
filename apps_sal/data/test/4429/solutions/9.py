import math as mt 
import sys,string
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
from collections import defaultdict



t=I()
for i in range(t):
    x,y,z=M()
    d=[x,y,z]
    p=max(x,y,z)
    c=0
    for j in d:
        if(j==p):
            c+=1
    if(c>=2):
        print("YES")
        if(c==2):
            print(min(x,y,z),min(x,y,z),p)
        else:
            print(p,p,p)
    else:
        print("NO")

