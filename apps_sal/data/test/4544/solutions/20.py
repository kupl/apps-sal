N=int(input())
a=list(map(int,input().split()))
res=0
count=[0]*(10**5+2)
for i in range(N) :
  count[a[i]]+=1
for i in range(10**5) :
  x=count[i]+count[i+1]+count[i-1]
  res=max(res,x)
print(res)
