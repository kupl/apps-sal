from math import *
from random import *
from copy import *
import os, sys

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
res = [0] * (n + 1)

for i in range(1, n + 1):
  prev = A[i - 1]
  res[i] = res[prev]
  prev = prev - k if prev == 0 else prev
  res[i] += min(max(0, i - prev - k - 1), k) + max(0, min(k + 1, n - i + 1) - max(0, min(n - prev + 1, prev + k - i + 1)))
print(' '.join(list(map(str, res[1 :]))))

