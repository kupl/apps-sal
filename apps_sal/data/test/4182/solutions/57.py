N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

Mx = max(x)
My = min(y)

if Mx >= My or Mx >= Y or X >= My:
  print("War")
else:
  print("No War")
