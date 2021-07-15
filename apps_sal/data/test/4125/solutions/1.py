import math
from functools import reduce
from sys import setrecursionlimit
setrecursionlimit(10**6)

def gcd(*numbers):
  return reduce(math.gcd, numbers)

n,x = map(int,input().split())
xl = list(map(int,input().split()))
xl = list(map(lambda y: abs(y-x), xl))

ans = -1
if len(xl) == 1:
    ans = xl[0]
else:
    ans = gcd(*xl)

print(ans)
