N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.reverse()
B.reverse()
count = 0
for i in range(N):
  if A[i] <= B[i]  <= A[i] + A[i+1]:
    count += B[i]
    A[i], A[i+1] = 0, A[i+1] - (B[i] - A[i])
  elif B[i] > A[i] + A[i+1]:
    count += A[i] + A[i+1]
    A[i], A[i+1] = 0, 0
  elif B[i] < A[i]:
    count += B[i]
    A[i] = A[i] - B[i]
print(count)
