n,k=map(int, input().split())
if n-1 <= k:
  print(n-1)
else:
  cnt=k
  ans=k
  i=2
  while(cnt!= n-1):
    ans=ans+i
    cnt+=1
    i+=1
  print(ans)  
