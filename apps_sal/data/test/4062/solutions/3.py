import sys
a, b, c, d = map(int, input().split())
if a < 0 and b < 0:
  if c < 0:
    print(a * c)
    return
  else:
    print(b * c)
    return

if a < 0 and b >= 0:
  if c < 0 and d < 0:
    print(a * c)
  elif c < 0 and d >= 0:
    print(max(a * c, b * d))
  else:
    print(b * d)
  return
  
if c < 0 and d < 0:
    print(a * d)
else:
  print(b * d)
return
