x, y = map(int, input().split())
if x * y > 0:
  k = y + x
  if k > 0:
    print(0, k, k, 0)
  else:
    print(k, 0, 0, k)
else:
  k = y - x
  if k > 0:
    print(-k, 0, 0, k)
  else:
    print(0, k, -k, 0)
