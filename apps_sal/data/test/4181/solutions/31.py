n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
ans=0
for i in range(n):
  m = min(B[i], A[i])
  ans += m
  A[i] -= m
  B[i] -= m
  m = min(B[i], A[i+1])
  ans += m
  A[i+1] -= m
  B[i] -= m
print(ans)
