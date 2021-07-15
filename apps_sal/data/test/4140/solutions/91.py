N = list(map(int, list(input())))
p1 = 0
p2 = 0
flag = 0
for i in N:
  if i == flag:
    p1 += 1
  else:
    p2 += 1
  flag = 1 - flag
print(min(p1, p2))
