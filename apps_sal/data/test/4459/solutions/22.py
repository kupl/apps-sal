import collections as c
N,*A = map(int,open(0).read().split())
A = c.Counter(A)
ans=0
for a,n in A.items():
  if a<n:
    ans+=n-a
  elif a>n:
    ans+=n
print(ans)
