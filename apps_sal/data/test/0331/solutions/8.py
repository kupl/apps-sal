import heapq
from collections import deque
import sys

#
# f = open('input.txt')
# sys.stdin = f


n,m,k=map(int,input().split())
m-=1
s=list(map(int,input().split()))
d = n*2
for i in range(n):
    if s[i] and s[i]<=k:
        tmp=abs(i-m)
        if tmp<d:
            d=tmp
print(d*10)
