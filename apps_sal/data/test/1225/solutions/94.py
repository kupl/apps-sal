H = int(input())

if H == 1:
  print((1))
  return

import math as m
n = m.floor(m.log2(H))+1
ans = (2**n) - 1

print(ans)


