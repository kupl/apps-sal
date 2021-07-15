a, b = map(int,input().split())
if (a > b):
  a, b = b, a
if ((b - a)%2 == 0):
  print(a + (b - a)//2)
else:
  print("IMPOSSIBLE")
