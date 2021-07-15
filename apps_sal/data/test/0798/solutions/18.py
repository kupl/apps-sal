a, b, c = map(int, input().split())

n = abs(a - b)
if c < n or a + b < c or (c - n) % 2 != 0:
  print("Impossible")
else:
  m = (c - n) // 2
  if a > b:
    print(b - m, m, c - m)
  else:
    print(a - m, c - m, m)
