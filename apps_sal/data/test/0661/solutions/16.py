m, k = map(int, input().split())
if k >= 2**m:
  print(-1)
elif m == 0:
  print(0, 0)
elif m == 1:
  if k == 0:
    print(0, 0, 1, 1)
  else:
    print(-1)
else:
  for i in range(2**m):
    if i == k:
      continue
    print(i, end=" ")
  print(k, end=" ")
  for i in range(2**m-1, -1, -1):
    if i == k:
      continue
    print(i, end=" ")
  print(k)
