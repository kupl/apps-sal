n, a, b = map(int, input().split())

s = int(n*a)

if s >= b:
  print(b)
else:
  print(s)
