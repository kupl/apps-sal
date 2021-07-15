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

n, m, k = reads()
b = reads()

df = [b[k+1] - b[k] - 1 for k in range(n-1)]
df.sort()
ans = n + sum(df[:n-k])
print(ans)
