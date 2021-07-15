from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
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
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
#ts=time.time()
#sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
#show_flg=True


def solve(s):
    ans=0
    n=len(s)
    show(*s,n*(n-1)//2)
    t=[]
    if n==1:
        print(0)
        return
    if len(Counter(s))==1:
        print(n*(n-1)//2)
        return
    p=s[0]
    c=1
    
    for i in range(1,n):
        if s[i]==p:
            c+=1
        else:
            ans+=c
            p=s[i]
            t.append(c)
            c=1
        show('i,ans,c,p',i,ans,c,p)
    t.append(c)
    ans=0
    for i in range(len(t)-1):
        ans+=t[i]+t[i+1]-1
    show(ans,t)
    print(n*(n-1)//2-(ans))
    return ans
   
q=1
for _ in range(q):
    n=I()
    s=list(input())
    #s=[chr(random.randint(1,2)+96-32) for i in range(random.randint(1,6))]
    solve(s)



