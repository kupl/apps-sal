N = int(input())
A = list(map(int,input().split()))
count = 0
j = 1

for i in range(N):
  if A[i] == j:
    count += 1
    j += 1

if count != 0:
  print(N-count)
else:
  print(-1)
