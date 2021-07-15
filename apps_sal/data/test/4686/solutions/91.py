w = input()
ans = True
for i in w:
  cnt = 0
  for j in w:
    if i == j:
      cnt += 1
  if cnt % 2 != 0:
    ans = False
    break
    
if ans:
  print("Yes")
else:
  print("No")
