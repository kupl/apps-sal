from math import sqrt
from collections import defaultdict as dd
import sys
input=sys.stdin.readline
import bisect
t=int(input())
while t:
    #n=int(input())
    n,k=map(int,input().split())
    #l=list(map(int,input().split()))
    for i in range(2,n+1):
        if(n%i==0):
            ind=i
            break
    n=n+i
    n=(k-1)*2+n
    print(n)
    t-=1
