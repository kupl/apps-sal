s, p = list(map(int, input().split()))

import math
tmp = s * s - 4 * p
if tmp < 0:
  print('No')
  return
m1 = (s + math.sqrt(tmp)) / 2
m2 = (s - math.sqrt(tmp)) / 2
if tmp == int(tmp):
  if m1 == int(m1) and m1 > 0:
    if s - int(m1) > 0:
      print('Yes')
      return
  if m2 == int(m2) and m2 > 0:
    if s - int(m2) > 0:
      print('Yes')
      return
print('No')

