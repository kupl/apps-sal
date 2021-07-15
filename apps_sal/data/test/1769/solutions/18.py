mod = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
uh=ii()
dh=ii()
n=uh+dh+1
for i in range(uh):
    print(i+1,end=' ')
print(n,end=' ')
for i in range(n-1,n-1-dh,-1):
    print(i,end=' ')
