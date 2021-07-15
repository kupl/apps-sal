N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
  if B[i] >= A[i]:
    B[i] -= A[i]
    ans += A[i]
    if B[i] >= A[i+1]:
      ans += A[i+1]
      A[i+1] = 0
    else:
      ans += B[i]
      A[i+1] -= B[i]
  else:
    ans += B[i]
print(ans)    
