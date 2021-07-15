ans = 'Yes'
c = []
for _ in range(3):
  c.append(list(map(int, input().split())))
adiff = []
bdiff = []
for i in range(2):
  adiff.append(c[i+1][0] - c[i][0])
  bdiff.append(c[0][i+1] - c[0][i])
for i in range(1, 3):
  for j in range(1, 3):
    if adiff[i-1] != c[i][j] - c[i-1][j] or bdiff[j-1] != c[i][j] - c[i][j-1]:
      ans = 'No'
      break
print(ans)

