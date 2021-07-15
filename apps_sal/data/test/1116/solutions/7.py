from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
#import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def ItoS(nn):
    return chr(nn+97)
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
show_flg=True

OR=['OBEY','REBEL']

def gcd(x,y):
    y,x=max(x,y),min(x,y)
    if y%x==0:
        return x
    return gcd(x,y%x)
    
t=I()
for _ in range(t):
    ans=0
    r,b,k=LI()
    r,b=max(r,b),min(r,b)
    
    g=gcd(r,b)
    r,b=r//g,b//g
    
    if (r-2)//b>=k-1:
        if r==b and k==1:
            a=0
        else:
            a=1
    else:
        a=0
    print(OR[a])
    
