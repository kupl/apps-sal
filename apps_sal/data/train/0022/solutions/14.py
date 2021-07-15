import sys
input=sys.stdin.readline
from collections import defaultdict as dd,deque as dq
t=int(input())
while t:
    #n=int(input())
    n,k=map(int,input().split())
    #l=list(map(int,input().split())
    k-=1
    while k:
        l=str(n).strip()
        x=int(min(l))*int(max(l))
        if(x==0):
            break
        n=n+x
        k-=1
    print(n)
    t-=1
