N,K=list(map(int,input().split()))
count=[0]*(100001)
for i in range(1,N+1) :
  a,b=list(map(int,input().split()))
  count[a]+=b
for i in range(1,100001) :
  if K<=count[i] :
    print(i)
    break
  K-=count[i]

