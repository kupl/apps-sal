#import resource
import sys
#resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
mod=(10**9)+7
#fact=[1]
#for i in range(1,1001):
#    fact.append((fact[-1]*i)%mod)
#ifact=[0]*1001
#ifact[1000]=pow(fact[1000],mod-2,mod)
#for i in range(1000,0,-1):
#    ifact[i-1]=(i*ifact[i])%mod
from sys import stdin, stdout
#from bisect import bisect_left as bl
#from bisect import bisect_right as br
#import itertools
#import math
#import heapq
#from random import randint as rn
#from Queue import Queue as Q
def modinv(n,p):
    return pow(n,p-2,p)
def ncr(n,r,p):
    t=((fact[n])*((ifact[r]*ifact[n-r])%p))%p
    return t
def ain():
    return list(map(int,sin().split()))
def sin():
    return stdin.readline()
def GCD(x, y):
   while(y):
       x, y = y, x % y
   return x
"""**************************************************************************"""
def merge1(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0]*n1
    R = [0]*n2
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i,j,k=0,0,l
    while i < n1 and j < n2 :
        if L[i][1] < R[j][1]:
            arr[k] = L[i]
            i += 1
        elif L[i][1] > R[j][1]:
            arr[k] = R[j]
            j += 1
        else:
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergesort1(arr,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergesort1(arr, l, m)
        mergesort1(arr, m+1, r)
        merge1(arr, l, m, r)
def merge2(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0]*n1
    R = [0]*n2
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i,j,k=0,0,l
    while i < n1 and j < n2 :
        if L[i][0] > R[j][0]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergesort2(arr,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergesort2(arr, l, m)
        mergesort2(arr, m+1, r)
        merge2(arr, l, m, r)
n,k=ain()
b=[]
for i in range(n):
    b.append(ain())
mergesort1(b,0,n-1)
r=[]
for i in range(n):
    r.append([b[i][0],i])
mergesort2(r,0,n-1)
g=[0]*n
s=0
for i in range(k):
    s+=r[i][0]
    g[r[i][1]]=1
p=k
s1=0
for i in range(n):
    q=s*b[i][1]
    s1=max(s1,q)
    if(g[i]==1):
        s-=b[i][0]
        while(p<n):
            if(r[p][1]>i):
                s+=r[p][0]
                g[r[p][1]]=1
                p+=1
                break
            p+=1
print (s1)

