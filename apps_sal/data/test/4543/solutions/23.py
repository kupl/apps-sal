import math
a, b = map(str, input().split())

s = a + b
s = int(s)
r = math.sqrt(s)
fr = r - int(r)
if fr == 0:
  print('Yes')
else:
  print('No')
