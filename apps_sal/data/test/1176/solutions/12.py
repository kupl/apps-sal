N = int(input())
A = list(map(int, input().split()))
ans = 0
Amin = 10 ** 9 + 1
flag = 0
for i in range(N):
  if i < N-1 and A[i] < 0:
    A[i] = -A[i]
    A[i+1] = -A[i+1]
  elif i == N-1 and A[i] < 0:
    A[i] = -A[i]
    flag = -1
    
  ans += A[i]
  
  if A[i] < Amin:
    Amin = A[i]
    
print((ans + (flag * 2 * Amin)))



