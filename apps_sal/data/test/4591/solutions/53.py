a,b,c,x,y = [int(x) for x in input().split()]
res = 0
if a + b > 2 * c:
  res += min(x,y) * 2 * c
  if x == min(x,y):
    if b > 2 * c:
      res += (y - min(x,y)) * 2 * c
    else:
      res += (y - min(x,y)) * b
  else:
    if a > 2 * c:
      res += (x - min(x,y)) * 2 * c
    else:
      res += (x - min(x,y)) * a
else:
  res += a * x
  res += b * y
print(res)
