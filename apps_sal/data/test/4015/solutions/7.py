n, m = (list(map(int, input().split())))
if m % n != 0:
  print(-1)
else:
  m //= n
  t = 0
  while m % 2 == 0:
    m //= 2
    t += 1
  while m % 3 == 0:
    t += 1
    m //= 3
  print(t if m == 1 else -1)

