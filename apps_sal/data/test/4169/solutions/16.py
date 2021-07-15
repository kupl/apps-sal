import sys
input = sys.stdin.readline # for speed up
#sys.setrecursionlimit(10**9)

n,m=list(map(int,input().split()))
a=[""]*n
for ii in range(n):
  a[ii]=list(map(int,input().split()))
a.sort()
r=0
for ii in range(n):
  if a[ii][1]>=m:
    r+=a[ii][0]*m
    print(r)
    return
  else:
    r+=a[ii][0]*a[ii][1]
    m-=a[ii][1]

