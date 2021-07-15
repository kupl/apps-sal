A = list(map(int,input().split()))
sums = sum(A)

for i in range(2 ** 4):
  res = 0
  for j in range(4):
    if (i >> j) & 1:
      res += A[j]
  if res == sums - res:
    print("Yes")
    break
else:
  print("No")
