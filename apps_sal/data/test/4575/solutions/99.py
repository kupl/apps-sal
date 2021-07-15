import sys
import copy
N=int(input())
a=[int(c) for c in input().split()]
D=a[0]
X=a[1]
a = [int(input()) for i in range(N)]

choco = 0
for i in range(N):
    cnt=0
    while cnt*a[i]+1<=D:
        choco+=1
        cnt+=1

print((choco+X))

