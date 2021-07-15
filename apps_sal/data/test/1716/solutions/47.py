n,m,q_=list(map(int,input().split()))
lr=[list(map(int,input().split())) for _ in range(m)]
pq=[list(map(int,input().split())) for _ in range(q_)]
from collections import defaultdict
dmap=defaultdict(int)
smap=defaultdict(int)
ssmap=defaultdict(int)
for l,r in lr:
  if (l,r) in dmap:
    dmap[(l,r)]+=1
  else:
    dmap[(l,r)]=1
for i in range(1,n+1):
  tmp=0
  for j in range(i,n+1):
    if (i,j) in dmap:
      tmp+=dmap[(i,j)]
    smap[(i,j)]=tmp
for i in range(1,n+1):
  tmp=0
  for j in range(1,i+1):
    tmp+=smap[(j,i)]
    ssmap[(j,i)]=tmp

for p,q in pq:
  ans=ssmap[(q,q)]-ssmap[(p-1,q)]
  print(ans)

