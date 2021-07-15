from itertools import *
N = int(input())
A = list(accumulate(map(int,input().split())))
l = 0
r = 2
t = A[-1]
a = t

for m in A[1:-2]:
  while abs(t-2*A[r]+m)>abs(t-2*A[r+1]+m):
    r+=1
  while abs(m-2*A[l])>abs(m-2*A[l+1]):
    l+=1
  x = sorted([A[l],m-A[l],A[r]-m,t-A[r]])
  a = min(a,x[3]-x[0])

print(a)
