c = [list(map(int, input().split())) for _ in range(3)]
for i in [1, 2]:
  d1 = c[0][0] - c[i][0]
  d2 = c[0][1] - c[i][1]
  d3 = c[0][2] - c[i][2]
  d4 = c[0][0] - c[0][i]
  d5 = c[1][0] - c[1][i]
  d6 = c[2][0] - c[2][i]
  if d1 != d2 or d1 != d3 or d4 != d5 or d4 != d6:
    print("No")
    return
print("Yes")
