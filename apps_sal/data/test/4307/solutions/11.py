N=int(input())
ans=0
for i in range(1,N+1,2):
  cnt=2
  for j in range(3,int(i**0.5)+1,2):
    if i%j==0:
      cnt+=2
  if cnt==8:
    ans+=1
print(ans)
