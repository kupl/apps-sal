a = list(map(int, input().split()))
x = abs(a[0]-a[1])
y = abs(a[1]-a[2])
z = abs(a[2]-a[0])
m = max(x, y, z)
if m == x:
  print(y+z)
elif m == y:
  print(x+z)
else:
  print(x+y)
