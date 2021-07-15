N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = sum(A)

for n in range(N):
  if A[n]>=B[n]:
    A[n]-=B[n]
  else:
    A[n+1] = max(0,A[n+1]+A[n]-B[n])
    A[n] = 0
    
print(M-sum(A))
