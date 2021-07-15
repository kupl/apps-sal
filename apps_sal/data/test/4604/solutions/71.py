from collections import Counter

n=int(input())
a=list(map(int,input().split()))

c=Counter(a)

if (n%2==0 and c[0]!=0) or (n%2==1 and c[0]!=1):
  print(0)
  return

ans=1
mod=10**9+7
for i in c:
  if c[i]==2:
    ans*=2
    ans%=mod
  if c[i]>=3:
    print(0)
    return

print(ans)
