n=int(input())
ans=float('inf')
for a in range(1,int(n**0.5+1)):
  if n%a==0:
    ans=min(ans,a+n//a-2)
print(ans)

