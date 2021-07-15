m, k = map(int, input().split())
if not (0<=k<2**m):
  print(-1)
  return
if m == 1:
  if k == 0:
    print(0, 0, 1, 1)
  else:
    print(-1)
else:
  L = []
  for i in range(2**m):
    if i != k:
      L.append(i)
  L.append(k)
  for i in range(2**m-1, -1, -1):
    if i != k:
      L.append(i)
  L.append(k)
  print(*L)
