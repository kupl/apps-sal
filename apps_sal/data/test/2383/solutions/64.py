N = int(input())
A = list(map(int, input().split()))
min = 1
check = True
count = 0
for i in range(N):
  if A[i] != min:
    A[i] = 0
    count += 1
  elif A[i] == min:
    min += 1
if A == [0] * N:
  print(-1)
else:
  print(count)
