a, b, x = map(int, input().split())
if a == x or (a + b >= x and a < x):
  print("YES")
else:
  print("NO")
