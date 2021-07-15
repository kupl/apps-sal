x = list(map(int,input().split()))
for i in range(3):
  for j in range(i+1,4):
    if x[i] > x[j]:
      x[i], x[j] = x[j], x[i]
if x[0]+x[1]+x[2] == x[3]:
  print("Yes")
  return
elif x[0]+x[3] == x[1]+x[2]:
  print("Yes")
  return
else:
  print("No")
