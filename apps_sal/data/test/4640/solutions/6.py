import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br


"""
Facts and Data representation
Constructive? Top bottom up down
"""
def solve():
  n, k = I()
  a = I()
  y = I()
  a.sort()
  max_till = [0] * (2 * n)  
  ans = 0
  for i in range(n - 1, -1, -1):
    left, right = a[i], a[i] + k
    idxR = br(a, right)
    idxL = bl(a, left)
    cur = (idxR - idxL)
    max_till[i] = max(max_till[i + 1], cur)
    ans = max(ans, cur + max_till[idxR])
  print(ans)

t, = I()
while t:
  t -= 1
  solve()
