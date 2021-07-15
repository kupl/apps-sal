N=int(input())
A=list(map(int,input().split()))

if N == 2:
  print(*(max(A),min(A)))
  return
  
m = max(A)/2
nearest=-1
for i in range(N):
  if abs(A[i]-m)<abs(nearest-m):
    nearest = A[i]

print(*(max(A),nearest))
