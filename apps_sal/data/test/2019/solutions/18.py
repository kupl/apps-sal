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
  s = input()
  stack = []
  cnt = 0
  for i in range(len(s)):
    if stack and stack[-1] != s[i]:
      cnt += 1
      stack.pop()
      continue
    stack.append(s[i])
  if cnt % 2:
    print('DA')
  else:
    print('NET')

t, = I()
while t:
  t -= 1
  solve()
