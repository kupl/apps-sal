N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i, a in enumerate(A, 1):
  if a == i:
    if i != len(A):
      x = A[i - 1]
      y = A[i]
      A[i - 1] = y
      A[i] = x    
      cnt += 1
    else:
      x = A[i - 2]
      y = A[i - 1]
      A[i - 2] = y
      A[i - 1] = x    
      cnt += 1
print(cnt)
