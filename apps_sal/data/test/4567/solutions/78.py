n = int(input())
x = 0
mn = 100
for i in range(n):
  s = int(input())
  x += s
  if s % 10 != 0:
    if s <= mn:
      mn = s
if x % 10 != 0:
  print(x)
else:
  x -= mn
  if x % 10 == 0:
    print((0))
  else:
    if x < 0:
      print((0))
      return
    print(x)

