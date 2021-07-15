x, a, b = list(map(int, input().split()))
p = b - a
if p <= 0:
  print("delicious")
elif x >= p:
  print("safe")
else:
  print("dangerous")

