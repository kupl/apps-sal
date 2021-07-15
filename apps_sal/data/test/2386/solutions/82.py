N=int(input())
A=list(map(int,input().split()))
for i in range(N):
  A[i]=A[i]-(i+1)
A.sort()
ans=0
anssub=A[N//2]
for i in range(N):
  ans+=abs(A[i]-anssub)
print(ans)  
