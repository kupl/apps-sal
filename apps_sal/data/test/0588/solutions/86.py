#解説解法
n = int(input())
xp = []
xm = []
yp = []
ym = []
for _ in range(n):
  x,y = map(int,input().split())
  if x == 0:
    if y == 0:
      n -= 1
    elif y > 0:
      yp.append([0,x,y])
    else:
      ym.append([0,x,y])
  elif x > 0:
    xp.append([y/x,x,y])
  else:
    xm.append([y/x,x,y])
xp.sort()
xm.sort()
xy = xp + yp + xm + ym
can = []
for i in range(-n,0):
  X = 0
  Y = 0
  for j in range(i+1,i+n+1):
    x,y = xy[j][1],xy[j][2]
    X += x
    Y += y
    can.append(X**2+Y**2)
if n == 0:
  print(0)
else:
  print(max(can)**.5)
