N, M = map(int, input().split())
A = list(map(lambda x: int(x)//2, input().split()))

import math

def lcm(x, y):
  return (x // math.gcd(x, y)) * y

def pow2(x):
  ret = 0
  while x%2 == 0:
    ret += 1
    x //= 2
  return ret

P = []
for a in A:
  P.append(pow2(a))

if len(set(P)) != 1:
  print(0)
else:
  m = 1
  for a in A:
    m = lcm(m, a)
  print(-(-(M//m)//2))
