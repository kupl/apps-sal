a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

c = [[0]*3 for _ in range(3)]

for k in range(n):
  for i in range(3):
    for j in range(3):
      if a[i][j] == b[k]:
        c[i][j] += 1
        
for i in range(3):
  if c[0][i] == c[1][i] == c[2][i] == 1:
    print("Yes")
    return
for j in range(3):
  if c[j][0] == c[j][1] == c[j][2] == 1:
    print("Yes")
    return
if c[0][0] == c[1][1] == c[2][2] == 1:
  print("Yes")
  return
if c[0][2] == c[1][1] == c[2][0] == 1:
  print("Yes")
  return
print("No")
