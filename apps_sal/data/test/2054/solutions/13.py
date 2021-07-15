import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br

def solve():
  a, b = I()
  if a > b:
    a, b = b, a
  print(min(a, (a + b) // 3))

t, = I()
while t:
  t -= 1
  solve()
