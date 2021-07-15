X, Y = map(int,input().split())
ans = False
for i in range(X + 1):
  if 2 * i + 4 * (X - i) == Y:
    ans = True
if ans:
  print("Yes")
else:
  print("No")
