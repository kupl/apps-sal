n,m=list(map(int,input().split()))
pre=[[] for i in range(n)]
pre_num=[[] for i in range(n)]
city=[]

for i in range(m):
  #pの県に属してy年にできた
  p,y=list(map(int,input().split()))
  pre[p-1].append(y)
  city.append(p-1)

from bisect import bisect_right

for i in range(n):
  town=sorted(pre[i])
  for j in range(len(town)):
    pre_num[i].append(bisect_right(town,pre[i][j]))

cnt=[0 for i in range(n)]
for i in city:
  print((str(i+1).zfill(6)+str(pre_num[i][cnt[i]]).zfill(6)))
  cnt[i]+=1
  


  

