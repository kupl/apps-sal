n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
if n>=m:
  print(0)
  return
data=[0]*(m-1)
for i in range(m-1):
  data[i]=x[i+1]-x[i]
data.sort()
res=0
for i in range(n-1):
  res+=data[m-2-i]
print(sum(data)-res)
