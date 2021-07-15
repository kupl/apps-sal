N = int(input())
A = list(map(int,input().split()))
ans = 0
ls = []
ans = 0
for i in range(N):
  if i == N-1:
    if A[i] == i+1:
      A[i],A[i-1] = A[i-1],A[i]
      ans += 1
  else:
    if A[i] == i+1:
      A[i],A[i+1] = A[i+1],A[i]
      ans += 1
print(ans)
