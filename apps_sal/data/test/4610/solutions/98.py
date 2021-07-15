import collections
N,K=map(int,input().split())
a=list(map(int,input().split()))
c=collections.Counter(a)
l=len(c)
c=list(c.items())
c.sort(key=lambda x: x[1])
ans=0
for i in c:
  if l<=K:
    break
  ans+=i[1]
  l-=1
print(ans)
