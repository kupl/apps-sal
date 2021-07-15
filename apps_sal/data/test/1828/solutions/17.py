n = int(input())
sx, sy = (int(x) for x in input().split())
ax, ay = sx, sy
bx, by = (int(x) for x in input().split())
cx, cy = (int(x) for x in input().split())

ans = 0

for i in range(n - 3):
  fx = bx - ax
  fy = by - ay
  lx = cx - bx
  ly = cy - by
  if fx != 0: fx = fx/abs(fx)
  if fy != 0: fy = fy/abs(fy)
  if lx != 0: lx = lx/abs(lx)
  if ly != 0: ly = ly/abs(ly)
  if (fy ==  1 and lx == -1): ans += 1
  if (fx ==  1 and ly ==  1): ans += 1
  if (fy == -1 and lx ==  1): ans += 1
  if (fx == -1 and ly == -1): ans += 1


  ax, ay = bx, by
  bx, by = cx, cy
  cx, cy = (int(x) for x in input().split())

fx = bx - ax
fy = by - ay
lx = cx - bx
ly = cy - by
if fx != 0: fx = fx/abs(fx)
if fy != 0: fy = fy/abs(fy)
if lx != 0: lx = lx/abs(lx)
if ly != 0: ly = ly/abs(ly)
if (fy ==  1 and lx == -1): ans += 1
if (fx ==  1 and ly ==  1): ans += 1
if (fy == -1 and lx ==  1): ans += 1
if (fx == -1 and ly == -1): ans += 1


ax, ay = bx, by
bx, by = cx, cy
cx, cy = sx, sy

fx = bx - ax
fy = by - ay
lx = cx - bx
ly = cy - by
if fx != 0: fx = fx/abs(fx)
if fy != 0: fy = fy/abs(fy)
if lx != 0: lx = lx/abs(lx)
if ly != 0: ly = ly/abs(ly)
if (fy ==  1 and lx == -1): ans += 1
if (fx ==  1 and ly ==  1): ans += 1
if (fy == -1 and lx ==  1): ans += 1
if (fx == -1 and ly == -1): ans += 1


print(ans)
