import math

N=int(input())
A=list(map(int,input().split()))
L=[0]*(N+1)
R=[0]*(N+1)
M=[0]*N
for i in range(N):
  L[i+1]=math.gcd(L[i],A[i])
for i in range(N-1,0,-1):
  R[i]=math.gcd(R[i+1],A[i])
for i in range(N):
  M[i]=math.gcd(L[i],R[i+1])
print(max(M))
