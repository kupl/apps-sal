n=int(input())
A = []
for i in range(5):
  A.append(int(input()))

minA = min(A)

import math
print(4+math.ceil(n/minA))
