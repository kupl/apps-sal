N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(N):
  x = A[i] - 1
  ans += B[x]
  if i >= 1 and A[i] == A[i-1] + 1:
    ans += C[A[i-1]-1]
print(ans)
