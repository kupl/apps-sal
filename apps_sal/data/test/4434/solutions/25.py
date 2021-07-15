import sys
input=sys.stdin.readline
from collections import defaultdict as dd
t=int(input())
while t:
    n=int(input())
    a=8
    res=0
    for i in range(1,n//2+1):
        res+=a*i*i
    print(res)
    t-=1
