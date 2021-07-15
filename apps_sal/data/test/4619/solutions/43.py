w,h,n = list(map(int,input().split()))
xl = []
yl = []
al = []
for _ in range(n):
  x,y,a = list(map(int,input().split()))
  xl.append(x)
  yl.append(y)
  al.append(a)

sx = 0
gx = w
sy = 0
gy = h

for i in range(len(al)):
  if al[i] == 1 and sx < xl[i]:
      sx = xl[i]
      if sx > gx:
        print((0))
        return
  elif al[i] == 2 and gx > xl[i]:
      gx = xl[i]
      if sx > gx:
        print((0))
        return
  elif al[i] == 3 and sy < yl[i]:
      sy = yl[i]
      if sy > gy:
        print((0))
        return
  elif al[i] == 4 and gy > yl[i]:
      gy = yl[i]
      if sy > gy:
        print((0))
        return
  if i == len(al)-1:
    print(((gx-sx)*(gy-sy)))
    

