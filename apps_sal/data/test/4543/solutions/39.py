import math
a, b = input().split()

if math.sqrt(int(a + b)) == int(math.sqrt(int(a + b))):
  print('Yes')
else:
  print('No')
