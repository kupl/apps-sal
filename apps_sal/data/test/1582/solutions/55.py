N=int(input())
d={}
for i in range(1,10):
  for j in range(1,10):
    d[i*10+j]=0
for i in range(1,min(10,N+1)):
  d[i*10+i]=1
for i in range(11,N+1):
  i=str(i)
  h,t=int(i[0])*10,int(i[-1])
  if t!=0:
    d[h+t]+=1
ans=0
for i in range(1,9):
  for j in range(i+1,10):
    ans+=(d[i*10+j]*d[j*10+i])*2
for i in range(1,10):
  ans+=d[i*10+i]**2
print(ans)
