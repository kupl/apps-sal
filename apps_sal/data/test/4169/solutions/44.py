n,m=map(int,input().split())
ab=[]
for i in range(n):
  a,b=map(int,input().split())
  ab.append([a,b])
ab.sort()
ans=0
t=m
for i in range(n):
  if ab[i][1]<t:
    ans+=ab[i][0]*ab[i][1]
    t-=ab[i][1]
  else:
    ans+=ab[i][0]*t
    print(ans)
    return
