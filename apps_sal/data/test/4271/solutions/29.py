N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0

for i in range(N):
  ans += B[A[i]-1]
  
  
for j in range(0, N-1):
  if A[j+1] == A[j] + 1:
    ans = ans + C[A[j]-1]
    
print(ans)
  

