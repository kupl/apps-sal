import math

n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
args = sorted([(math.atan2(y,x),x,y) for x,y in xy])
ans = 0
for key,(sarg,sx,sy) in enumerate(args):
  tmpx,tmpy = sx,sy
  dist = tmpx**2 + tmpy**2
  for arg,x,y in args[key+1:]:
    tmpx += x
    tmpy += y
    tmp = tmpx**2 + tmpy**2
    if tmp < dist:
      break
    else:
      dist = tmp
  for arg,x,y in args[:key]:
    tmpx += x
    tmpy += y
    tmp = tmpx**2 + tmpy**2
    if tmp < dist:
      break
    else:
      dist = tmp
  ans = max(ans,dist)
print(math.sqrt(ans))
