N=int(input())
red=[]
blue=[]
for _ in range(N):
  a,b = map(int,input().split())
  red.append((a+1,b+1))
for _ in range(N):
  c,d = map(int,input().split())
  blue.append((c+1,d+1))

blue.sort(key=lambda x:x[0])
for b in blue:
  c = None
  bx, by = b
  for r in red:
    rx, ry = r
    if rx < bx and ry < by:
      if c is None or c[1] < ry:
        c = r
  if c:
    red.remove(c)

print(N-len(red))
