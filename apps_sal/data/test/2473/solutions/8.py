# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

#n = int(input())
#n,a = [int(i) for i in readline().split()]
n,k = [int(i) for i in readline().split()]
xy = [[int(i) for i in readline().split()] for i in range(n)]

xy.sort()
#print(xy)
ans = 4*10**18+10
for i in range(n):
    for j in range(i+k-1,n):
        dx = xy[j][0] - xy[i][0]
        y = sorted(xy[k][1] for k in range(i,j+1))
#        print(y,i,j)
        L = len(y)-k+1
        for i in range(L):
            dy = y[i+k-1]-y[i]
            ans = min(ans,dy*dx)
        


print(ans)
