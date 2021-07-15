import sys
input = sys.stdin.readline # for speed up
sys.setrecursionlimit(10**7)

n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

aa=[0]*(len(a)+1)
bb=[0]*(len(b)+1)

for ii in range(len(a)):
  aa[ii+1]=aa[ii]+a[ii]
for ii in range(len(b)):
  bb[ii+1]=bb[ii]+b[ii]
"""
print(a)
print(aa)
print(b)
print(bb)
"""
r=0
jmax=len(bb)-1
for ii in range(len(aa)):
  if aa[ii]>k:
    break
  for jj in range(jmax,-1,-1):
    if bb[jj]>k-aa[ii]:
      pass
    else:
      r=max(r,ii+jj)
      #print(r,ii,jj)
      jmax=jj
      break
print(r)

