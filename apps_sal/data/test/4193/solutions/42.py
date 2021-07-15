a = [list(map(int,input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]
for i in range(3):
  for j in range(3):
    if a[i][j] in b:
      a[i][j] = "o"
for i in range(3):
  if a[i][0] == a[i][1] == a[i][2]:
    print("Yes")
    return
  elif a[0][i] == a[1][i] == a[2][i]:
    print("Yes")
    return
  elif a[0][0] == a[1][1] == a[2][2]:
    print("Yes")
    return
  elif a[0][2] == a[1][1] == a[2][0]:
    print("Yes")
    return
  elif i == 2:
    print("No")
