from itertools import *
from collections import defaultdict
def ints():
  return [int(x) for x in input().split()]
def readi():
  return int(input())

N, K = ints()
A = ints()
S = [0] + list(accumulate(A))

def f(i):
  return (S[i]-i)%K

s = 0
memo = defaultdict(int)
for j in range(1, N+1):
  fj = f(j)

  if j-K>=0:
    memo[f(j-K)] -= 1
  memo[f(j-1)] += 1

  s += memo[fj]
print(s)

