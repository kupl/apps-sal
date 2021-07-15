import sys
n = int(input())
xyh = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n):
  if xyh[i][2] != 0:
    cnt += 1
if cnt == 1:
  for i in range(n):
    if xyh[i][2] != 0:
      print(" ".join(list(map(str, xyh[i]))))
      return
for i in range(101):
  for j in range(101):
    x = []
    for k in range(n):
      if xyh[k][2] != 0:
        x.append(abs(xyh[k][0]-i)+abs(xyh[k][1]-j)+xyh[k][2])
    if len(set(x)) == 1:
      print(i, j, x[0])
