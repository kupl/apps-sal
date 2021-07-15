n,m=map(int,input().split())
A = list(map(int, input().split()))
k=A[0]-1
for i in range(1,m):
   if A[i]>A[i-1]:
      k+=A[i]-A[i-1]
   if A[i]<A[i-1]:
      k+=n+A[i]-A[i-1]
print(k) 
