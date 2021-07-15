n,m=map(int,input().split())


citylis=[[] for i in range(n)]
for i in range(1,m+1):
  pi,yi=map(int,input().split())
  citylis[pi-1].append([i,yi])

for i in range(n):
  if len(citylis[i])!=0:
    citylis[i].sort(key=lambda x:x[1])

lis=[]
for i in range(n):
  for j in range(len(citylis[i])):
    cityposi=str(i+1)
    cityposi="0"*(6-len(cityposi))+cityposi
    ordernum=str(j+1)
    ordernum="0"*(6-len(ordernum))+ordernum
    lis.append([citylis[i][j][0],cityposi+ordernum])

lis.sort(key=lambda x:x[0])
for i in range(m):
  print(lis[i][1])
