X = int(input())

import math as m

t = int(m.sqrt(X*2))
if t*(t+1)/2 < X:
  t += 1

print(t)
