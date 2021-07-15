mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
  x, y, z = map(int, input().split())
  mat[i][0] = x
  mat[i][1] = y
  mat[i][2] = z

n = int(input())

for i in range(n):
  x = int(input())
  for j in range(3):
    for k in range(3):
      if mat[j][k] == x:
        mat[j][k] = -1
        break

if mat[0][0] == -1 and mat[0][1] == -1 and mat[0][2] == -1:
  print("Yes")
  return
elif mat[1][0] == -1 and mat[1][1] == -1 and mat[1][2] == -1:
  print("Yes")
  return
elif mat[2][0] == -1 and mat[2][1] == -1 and mat[2][2] == -1:
  print("Yes")
  return
elif mat[0][0] == -1 and mat[1][0] == -1 and mat[2][0] == -1:
  print("Yes")
  return
elif mat[0][1] == -1 and mat[1][1] == -1 and mat[2][1] == -1:
  print("Yes")
  return
elif mat[0][2] == -1 and mat[1][2] == -1 and mat[2][2] == -1:
  print("Yes")
  return
elif mat[0][0] == -1 and mat[1][1] == -1 and mat[2][2] == -1:
  print("Yes")
  return
elif mat[2][0] == -1 and mat[1][1] == -1 and mat[0][2] == -1:
  print("Yes")
  return
else:
  print("No")
