from heapq import heappop,heappush
q=int(input())
queries=[list(map(int,input().split()))for _ in range(q)]
l=[]
r=[]
ans=0
quecount=0
for query in queries:
  if query[0]==1:
    quecount+=1
    _,a,b=query
    ans+=b
    if quecount==1:
      mid=a
    elif quecount%2==1:
      if a<-l[0]:
        mid=-heappop(l)
        heappush(l,-a)
      elif r[0]<a:
        mid=heappop(r)
        heappush(r,a)
      else:
        mid=a
      ans+=abs(a-mid)
    else:
      ans+=abs(a-mid)
      heappush(l,-min(a,mid))
      heappush(r,max(a,mid))
  if query[0]==2:
    if quecount%2==1:
      ansind=mid
    else:
      ansind=-l[0]
    print(ansind,ans)
