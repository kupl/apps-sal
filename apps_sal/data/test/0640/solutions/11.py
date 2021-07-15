a, b = list(map(int, input().split()))
if a == b: x, y, z = 0, 6, 0
else:
  y = 1-abs(a-b)%2
  if (a < b):
    x = a+(b-a-1)//2
    z = 6-x-y
  else:
    z = b+(a-b-1)//2
    x = 6-z-y

print("{} {} {}".format(x, y, z))

