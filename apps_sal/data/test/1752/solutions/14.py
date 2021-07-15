import sys,math,string
input=sys.stdin.readline
from collections import deque
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))

n=int(input())
l=L()
l.sort()
g=deque([])
for i in range(n):
    if(i%2==0):
        g.append(l[i])
    else:
        g.appendleft(l[i])
print(*g)

