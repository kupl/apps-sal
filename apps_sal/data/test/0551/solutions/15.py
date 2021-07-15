n = int(input())
P = list(enumerate(map(int,input().split())))

from fractions import gcd


def check(i,j):
  x0,y0 = P[i]
  x1,y1 = P[j]

  dx = x1-x0
  dy = y1-y0
  offsets = [dx*y0-dy*x0]

  for x,y in P:
    o = dx*y-dy*x
    if o not in offsets:
      offsets.append(o)
      if len(offsets) > 2:
        return False

  return len(offsets) == 2
  
print('Yes' if any(check(i,j) for i,j in [(0,1),(1,2),(0,2)]) else 'No')
