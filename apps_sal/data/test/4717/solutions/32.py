x, a, b = list(map(int, input().split()))
if abs(x-a) > abs(x-b):
  print("B")
else:
  print("A")

