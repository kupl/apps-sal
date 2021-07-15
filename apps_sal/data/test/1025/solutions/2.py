from fractions import *
n,s=int(input()),0
p=[tuple(map(int, input().split())) for _ in range(n)]
def f(a,b): g=gcd(a,b);return a//g + 1024*1024*(b//g)
for i in range(n):
    k,(x,y)=0,p[i]
    l=sorted(f(x-X, y-Y) for X,Y in p[:i])
    for j in range(1, i):
        k=k+1 if l[j]==l[j-1] else 0
        s+=k
print(n*(n-1)*(n-2)//6-s)

