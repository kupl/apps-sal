n = int(input())
l = [(0,0,0)]
flag = 1
for i in range(n):
  l.append(list(map(int,input().split())))
for i in range(n):
  d = abs(l[i+1][1] - l[i][1]) + abs(l[i+1][2] - l[i][2])
  if l[i+1][0] - l[i][0] >= d and (l[i+1][0] - l[i][0] - d) % 2 == 0:
    continue
  else:
    flag = 0
if flag:
  print("Yes")
else:
  print("No")

  


