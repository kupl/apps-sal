import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.readline().split())
def Li():return list(map(int,sys.stdin.readline().split()))

n = Ii()
ans = 0
points = []
xymax = 0
xymin = 10**11
dxymax = -10**11
dxymin = 10**11
for i in range(n):
  point = Li()
  xy = point[0]+point[1]
  if xy > xymax:
    xymax = xy
  if xy < xymin:
    xymin = xy
  dxy = point[0]-point[1]
  if dxy > dxymax:
    dxymax = dxy
  if dxy < dxymin:
    dxymin = dxy
ans = max(dxymax-dxymin,xymax-xymin)
print(ans)
