from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from functools import *
from itertools import permutations,combinations,groupby
import sys
import bisect
import string
import math
import time
import random
def Golf():
    *a,=map(int,open(0))
def S_():
    return input()
def IS():
    return input().split()
def LS():
    return [i for i in input().split()]
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def NI(n):
    return [int(input()) for i in range(n)]
def NI_(n):
    return [int(input())-1 for i in range(n)]
def StoI():
    return [ord(i)-97 for i in input()]
def ItoS(nn):
    return chr(nn+97)
def LtoS(ls):
    return ''.join([chr(i+97) for i in ls])
def GI(V,E,Directed=False,index=0):
    org_inp=[]
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        org_inp.append(inp)
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[0],inp[2])
            bb=(inp[1],inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return g,org_inp
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0}):
#h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0}) # sample usage
    mp=[1]*(w+2)
    found={}
    for i in range(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[1]+[mp_def[j] for j in s]+[1]
    mp+=[1]*(w+2)
    return h+2,w+2,mp,found
def bit_combination(k,n=2):
    rt=[]
    for tb in range(n**k):
        s=[tb//(n**bt)%n for bt in range(k)]
        rt+=[s]
    return rt
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['YES','NO']
Yn=['Yes','No']

mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
#ts=time.time()
#sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
 
def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

show_flg=False
show_flg=True

ans=0

n=I()
m=LI()
tot=0
for i in range(n):
    l,r=[],[]
    
    tmp=m[i]
    p=m[i]
    
    # right
    for j in range(i+1,n):
        if m[j]<p:
            p=m[j]
        tmp+=p
        r+=[p]
    
    p=m[i]
    # left
    for j in range(i-1,-1,-1):
        if m[j]<p:
            p=m[j]
        tmp+=p
        l+=[p]
    
    if tmp>tot:
        tot=tmp
        ans=l[::-1]+[m[i]]+r
        
print(*ans)





