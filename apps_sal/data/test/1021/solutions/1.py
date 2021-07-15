from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect

setrecursionlimit(10**7)

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

n = read()
c = reads()
t = reads()

if c[0] != t[0] or c[-1] != t[-1]:
  print("No"); return

dc = [c[k+1] - c[k] for k in range(n-1)]
dt = [t[k+1] - t[k] for k in range(n-1)]

if sorted(dc) == sorted(dt):
  print("Yes")
else:
  print("No")
