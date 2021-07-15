x, y = map(int, input().split())
for i in range(1, x+1):
  if (4*i + 2*(x - i) == y) or (2*i + 4*(x - i) == y):
    print("Yes")
    return
print("No")
