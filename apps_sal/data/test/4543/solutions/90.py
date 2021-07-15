a, b = input().split()
ab = int(a+b)
import math
if math.sqrt(ab).is_integer():
  print('Yes')
else:
  print('No')
