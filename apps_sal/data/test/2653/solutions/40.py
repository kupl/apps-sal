import sys
sys.setrecursionlimit(10**9)
def f(p,q=-1):
  for i in c[p]:
    if i!=q:
      A[i]+=A[p]
      f(i,p)
n,q=map(int,input().split())
c=[[]for _ in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  c[a-1].append(b-1)
  c[b-1].append(a-1)
A=[0]*n
for _ in range(q):
  p,x=map(int,input().split())
  A[p-1]+=x
f(0)
print(*A)
