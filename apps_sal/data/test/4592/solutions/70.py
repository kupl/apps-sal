n=int(input())
m=10**9+7
p=[1 for i in range(10000)]
p[0]=0
p[1]=0
for i in range(2,n+1):
  if p[i]==1:
    for j in range(i*i,n+1,i):
        p[j]=0
ans=1
for i in range(2,n+1):
  if p[i]:
    c=0
    k=i
    while n//k>0:
      c=c+(n//k)%m
      k=k*i
    ans=(ans*((c+1)%m))%m
print((ans%m))
    
    
      
      

