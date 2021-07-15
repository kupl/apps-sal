X, Y = map(int, input().split())

flag = False
for i in range(100):
  for j in range(100):
    if i+j == X and 2*i+4*j == Y:
      flag = True

if flag:
  print("Yes")
else:
  print("No")
