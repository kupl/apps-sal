t=int(input())
for i in range(t):
  n,k=map(int,input().split())
  ans=n
  for i in range(2,n+1):
    if n%i==0:
      ans+=i
      break
  ans+=2*(k-1)
  print(ans)
