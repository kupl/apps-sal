import math
mod=998244353
N=int(input())
L=list(map(int,input().split()))
if sum(L)<2*(N-1):
  print(0)
  return
ans=1
for i in L:
  ans*=i
  ans%=mod
c=sum(L)
for i in range(N-2):
  ans*=c-N-i
  ans%=mod
ans%=mod
print(ans)
