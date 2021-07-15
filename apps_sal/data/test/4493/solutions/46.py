c = []
for _ in range(3):
  c.append(list(map(int, input().split())))
if c[0][1]-c[0][0] == c[1][1]-c[1][0] and c[2][1]-c[2][0] == c[1][1]-c[1][0] and c[0][2]-c[0][1] == c[1][2]-c[1][1] and c[2][2]-c[2][1] == c[1][2]-c[1][1]:
  print("Yes")
else:
  print("No")
