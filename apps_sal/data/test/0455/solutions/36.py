#19:32
n = int(input())
raw = []
eo = []
h = 30
for _ in range(n):
  x,y = map(int,input().split())
  raw.append([x,y])
  eo.append((x+y)%2)
if sum(eo) == 0:
  print(h+2)
  d = [2**(h-i) for i in range(h+1)]
  d.append(1)
  print(' '.join(map(str,d)))
elif sum(eo) == n:
  print(h+1)
  d = [2**(h-i) for i in range(h+1)]
  print(' '.join(map(str,d)))
else:
  print(-1)
  return
for xy in raw:
  x,y = xy
  scale = 2 ** h
  ans = ''
  while scale != 0:
    tmp = [[0,0,'U'],[0,1,'D'],[0,2,'R'],[0,3,'L']]
    tmp[0][0] =   x   ** 2 + (y-1) ** 2
    tmp[1][0] =   x   ** 2 + (y+1) ** 2
    tmp[2][0] = (x-1) ** 2 +   y   ** 2
    tmp[3][0] = (x+1) ** 2 +   y   ** 2
    d,dr = min(tmp)[1],min(tmp)[2]
    ans += dr
    if d == 0:
      y -= scale
    elif d == 1:
      y += scale
    elif d == 2:
      x -= scale
    else:
      x += scale
    scale //= 2
  if x+y != 0:
    if y == 1:
      ans += 'U'
    elif y == -1:
      ans += 'D'
    elif x == 1:
      ans += 'R'
    else:
      ans += 'L'
  print(ans)
