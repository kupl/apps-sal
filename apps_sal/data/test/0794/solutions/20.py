import sys,math,string
input=sys.stdin.readline
from collections import deque
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
n=int(input())
l=L()
p=set(l)
if(len(p)==1):
    print(-1)
else:
    l.sort()
    print(*l)

