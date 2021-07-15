import numpy as np

n,k=map(int,input().split())
a=[int(x) for x in input().split()]
f=[int(x) for x in input().split()]

a.sort()
f.sort(reverse=True)

a=np.array(a)
f=np.array(f)
s=a.sum()

l,u=-1,f[0]*a[-1]
while l+1<u:
  m=(l+u)//2
  if s-np.minimum(a,m//f).sum()<=k:
    u=m
  else:
    l=m

print(u)
