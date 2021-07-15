m, k = map(int, input().split())
if k >= 2**m:
  print(-1)
  return
if m == 0:
  print(0, 0)
elif m == 1:
  if k == 0:
    print(0, 1, 1, 0)
  else:
    print(-1)
else:
  b = [i for i in range(2**m) if i != k]
  c = b[::-1]
  A = b + [k] + c + [k]
  print(*A)
