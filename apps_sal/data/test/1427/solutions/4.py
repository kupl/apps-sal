import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))
DIV = 10 ** 9 + 7
import math

from functools import reduce

def lcm(a,b,):
  return (a // math.gcd(a,b)) * b

G = reduce(lcm, A)
ans = sum(map(lambda x:G // x, A))

print(ans % DIV)
