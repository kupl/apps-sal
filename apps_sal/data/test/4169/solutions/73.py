n,m=map(int,input().split())
l=[]
for _ in range(n):
  a,b=map(int,input().split())
  l.append([a,b])
l.sort()
ans=0
for a,b in l:
  ans+=min(b,m)*a
  m=max(0,m-b)
print(ans)
