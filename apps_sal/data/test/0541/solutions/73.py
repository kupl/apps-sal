n,m=map(int,input().split())
data=[]
for i in range(m):
  a,b=map(int,input().split())
  data.append([b,a])
data.sort()
r,l=data[0]
cnt=1
for i in range(1,m):
  if data[i][1]>=r:
    cnt+=1
    r,l=data[i]
  else:
    r=min(r,data[i][0])
    l=max(l,data[i][1])
print(cnt)
