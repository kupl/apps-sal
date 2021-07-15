t = int(input())

import math

ans=[0]*t

for i in range(t):
  n=int(input())
  theta=90/n
  temp=1/math.sin(math.radians(theta))
  ans[i]=temp*math.cos(math.radians(theta/2))


for i in range(t):
  print(format(ans[i], '.9f'))
