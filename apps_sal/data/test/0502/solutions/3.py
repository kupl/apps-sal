ax,ay,bx,by,cx,cy = map(int,input().split())

dx1, dy1 = ax-bx, ay-by
dx2, dy2 = bx-cx, by-cy

# parallel
if dx1*dy2 == dx2*dy1 or dx1**2+dy1**2 != dx2**2+dy2**2:
  print('No')
else:
  print('Yes')
