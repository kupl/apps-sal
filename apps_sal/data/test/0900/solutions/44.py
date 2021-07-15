import numpy as np
 
s = input()
p = np.array([0]*13)
p[0] = 1
 
amari = [[0]*13 for _ in range(13)]
for j in range(10):
  for i in range(13):
    amari[i][(i*10+j)%13] += 1
M = np.array(amari)
 
for si in range(len(s)):
  a = np.array([0]*13)
  if s[si] == '?':
    a = np.dot(p,M)
  else:
    c = int(s[si])
    for i in range(13):
      a[(i*10+c)%13] += p[i]
  p = np.mod(a,1000000007)
print(p[5])
