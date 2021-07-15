K = int(input())
A = 7
count = 1

for i in range(K):
  if A%K == 0:
    print(count)
    break
  count += 1
  A = (10*A + 7)%K
else:
  print("-1")
