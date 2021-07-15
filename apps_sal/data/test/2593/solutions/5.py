from math import *
from bisect import *
from collections import *
from random import *
from decimal import *
import sys
input=sys.stdin.readline
def inp():
    return int(input())
def st():
    return input().rstrip('\n')
def lis():
    return list(map(int,input().split()))
def ma():
    return list(map(int,input().split()))
t=int(input())
while(t):
    t-=1
    n=inp()
    a=lis()
    b=[0]*30
    for i in a:
        z=bin(i)[2:]
        z=z.zfill(30)
        for j in range(30):
            if(z[j]=='1'):
                b[j]+=1
                break
    s=0
    for i in b:
        s+=(i*(i-1))//2
    print(s)
    

