N, T = input().split()
N = int(N)
T = int(T)

import numpy as np

c = np.zeros(N)
t = np.zeros(N)

for i in range(N):
  c[i], t[i] = input().split()
  c[i] = int(c[i])
  t[i] = int(t[i])
  if t[i] > T :
    c[i] = 1001

if min(c) == 1001:
  print('TLE')
  
else:
  print((int(min(c))))

