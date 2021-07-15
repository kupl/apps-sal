a, b = map(int, input().split())


x = (a + b) / 2
if x % 1 == 0:
  print(int(x))
else:
  print(int(x + 1))
