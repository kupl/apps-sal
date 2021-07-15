N=int(input())
P=list(map(int,input().split()))

dist=[0]*N
for i in range(N):
  dist[i]=i+1-P[i]

ans=[]
lp=1
for i in range(N-1):
    ch=0
    for j in range(lp-1,N-1):
      if dist[j]<0 and dist[j+1]>0:
        ans.append(j+1)
        dj=dist[j]
        dist[j]=dist[j+1]-1
        dist[j+1]=dj+1
        ch=1
        lp=j
        break
    if ch==0:
      print(-1)
      return

for i in dist:
  if i!=0:
    print(-1)
    return

for a in ans:
  print(a)
