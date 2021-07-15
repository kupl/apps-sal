n=int(input())
a=list(map(int,input().split()))

b=[0 for i in range(10**5+1)]
for i in a:
  b[i]+=1

if (n%2==0 and b[0]!=0) or (n%2==1 and b[0]!=1):
  print(0)
  return

ans=1
mod=10**9+7
for i in b:
  if i==2:
    ans*=2
    ans%=mod
  if i>=3:
    print(0)
    return

print(ans)
