N=int(input())
red=[]
blue=[]
for _ in range(N):
  a,b = map(int,input().split())
  red.append((a,b))
for _ in range(N):
  c,d = map(int,input().split())
  blue.append((c,d))

blue.sort(key=lambda x:x[0])
for bx, by in blue:
  c = None
  for rx, ry in red:
    if rx < bx and ry < by:
      if c is None or c[1] < ry:
        c = (rx, ry)
  if c:
    red.remove(c)

print(N-len(red))
