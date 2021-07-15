from math import *

N=int(input())
A=list(map(int,input().split()))

ans=A[0]

for i in range(1,N):
  ans=gcd(ans,A[i])

print(ans)

