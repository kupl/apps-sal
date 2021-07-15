N = int(input())
A = list(map(int, input().split()))
n = 1
for i in range(N):
  if A[i] == n:
    n += 1
if n != 1:
  print(N + 1 - n)
else:
  print(-1)
