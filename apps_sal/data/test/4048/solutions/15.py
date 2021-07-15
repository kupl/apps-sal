n=int(input())
ans=float('inf')
a=1
while n**0.5>=a:
  if n%a==0:
    ans=min(ans,a+n//a-2)
  a+=1
print(ans)

