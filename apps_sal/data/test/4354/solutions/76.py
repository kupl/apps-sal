n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
cd=[list(map(int,input().split())) for _ in range(m)]
r=[]
for i in ab:
  x1,y1=i[0],i[1]
  temp=[]
  for j in cd:
    x2,y2=j[0],j[1]
    temp.append(abs(x1-x2)+abs(y1-y2))
  r.append(temp.index(min(temp))+1)
print(*r,sep='\n')
