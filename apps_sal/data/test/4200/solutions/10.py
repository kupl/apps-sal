N, M = map(int, input().split())
A = list(map(int, input().split()))

vote = sum(A)
for i in range(N):
  if(A[i] >= vote/(4*M)):
    A[i] = 1
  else:
    A[i] = 0

if(M <= sum(A)):
  print("Yes")
else:
  print("No")
