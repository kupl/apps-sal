c=[list(map(int,input().split())) for _ in range(3)]
a=[0,0,0]
b=[0,0,0]

for i in range(3):
  b[i] = c[0][i] - a[0]

for i in range(1,3):
  a[i] = c[i][0] - b[0]

for i in range(3):
  for j in range(3):
    if c[i][j] != a[i]+b[j]:
      print("No")
      return
print("Yes")
