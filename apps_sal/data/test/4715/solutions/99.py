a, b, c = list(map(int, input().split()))

if a == b:
  if b == c:
    print((1))
  else:
    print((2))
elif b == c:
  print((2))
elif a == c:
  print((2))
else:
  print((3))

