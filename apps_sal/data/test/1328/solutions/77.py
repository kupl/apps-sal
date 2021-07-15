n,ma,mb=list(map(int,input().split()))
item=[]
for i in range(n):
  item.append(tuple(map(int,input().split())))

d={(0,0):0}
for i in range(n):
  nd={}
  for j in d:
    if j in nd:
      nd[j]=min(nd[j],d[j])
    else:
      nd[j]=d[j]
    s=(j[0]+item[i][0],j[1]+item[i][1])
    if s in nd:
      nd[s]=min(nd[s],d[j]+item[i][2])
    else:
      nd[s]=d[j]+item[i][2]
  d=nd
m=10**9
for i in d:
  if i==(0,0):
    continue
  if i[0]*mb==i[1]*ma:
    m=min(m,d[i])
if m==10**9:
  m=-1

print(m)
