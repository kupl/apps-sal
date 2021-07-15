import sys,math,string,bisect
input=sys.stdin.readline
from collections import deque,defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
n=int(input())
for _ in range(n):
    k=I()
    g=[]
    l=[0]+L()
    for i in range(1,k+1):
        s=i
        c=1
        while(l[s]!=i):
            s=l[s]
            c+=1
        g.append(c)
    print(*g)
            

