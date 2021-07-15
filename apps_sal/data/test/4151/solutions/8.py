from sys import stdin, stdout
from math import *
from heapq import *
from collections import *

def main():
    n=int(stdin.readline())
    a=[int(x) for x in stdin.readline().split()]
    b=[2]*(n+2)
    maxR={}
    minL={}
    for i in range(n):
        x=a[i]
        maxR[x]=i
        minL[x]=minL.get(x,i)
    f=[0]*(n+2)
    for i in range(n):
        x=a[i]
        l=minL[x]
        r=maxR[x]
        if (l<r):
            if (r==l-1):
                b[r]=1
            else:
                f[l+1]=f[l+1]+1
                f[r+1]=f[r+1]-1
    res=1
    for i in range(1,n):
        f[i]=f[i]+f[i-1]
        if (f[i]>0):
            b[i]=1
        res=(res*b[i])%998244353 
    stdout.write(str(res))
    return 0

def __starting_point():
    main()
__starting_point()
