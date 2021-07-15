import collections
n,k=list(map(int,input().split()))
A=[int(i) for i in input().split()]
ans=float("inf")
D1,D2=collections.defaultdict(list),collections.defaultdict(int)
for i in range(n):
  a=A[i]
  c=0
  D1[a].append(c)
  D2[a]+=1
  while a>0:
    a//=2
    c+=1
    D1[a].append(c)
    D2[a]+=1
for i in range(max(A)+1):
  if D2[i]>=k:
    D1[i].sort()
    ans=min(ans,sum(D1[i][:k]))
print(ans)


