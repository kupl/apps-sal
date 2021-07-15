n,m = map(int, input().split(" "))
a = [list(input()) for i in range(n)]
b = [list(input()) for i in range(m)]
ch = m**2
for i in range(n-m+1):
  for j in range(n-m+1):
    if a[i][j] == b[0][0]:
      count = 0
      for k in range(m):
        for l in range(m):
          #print(i+k, j+l)
          if a[i+k][j+l] == b[k][l]:
            count += 1
      if count == ch:
        print("Yes")
        break
  else:
    continue
  break
else:
  print("No")
