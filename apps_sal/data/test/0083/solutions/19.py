import sys,math,string
input=sys.stdin.readline
from collections import deque
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
n=int(input())
l=L()
cp=0
cn=0
cz=0
for i in range(n):
    if(l[i]>0):
        cp+=1
    elif(l[i]<0):
        cn+=1
    else:
        cz+=1
if(cp>=(n//2 +(n%2))):
    print(1)
elif(cn>=(n//2 +(n%2))):
    print(-1)
else:
    print(0)

