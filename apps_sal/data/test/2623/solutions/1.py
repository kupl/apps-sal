import sys
from collections import defaultdict
from copy import copy

R = lambda t = int: t(input())
RL = lambda t = int: [t(x) for x in input().split()]
RLL = lambda n, t = int: [RL(t) for _ in range(n)]


def solve():
  n, k = RL()
  s = sorted(R(str))
  if n == k:
    print(s[-1])
    return
  if s[0] < s[k-1]:
    print(s[k-1])
    return
  if s[-1] == s[k]:
    print(s[0] + "".join(s[k:][:(n-1)//k]))
    return
  print(s[0] + "".join(s[k:]))
  
T = R()
for _ in range(T):
  solve()

