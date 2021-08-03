from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque, Counter
from operator import mul
from functools import reduce


x, y, a, b, c = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p = sorted(p, reverse=True)[:x]
q = sorted(q, reverse=True)[:y]
r = sorted(r, reverse=True)

pq = sorted(p + q)
ans = sum(pq)

for i in range(len(r)):
    if pq[i] < r[i]:
        ans = ans + r[i] - pq[i]
    else:
        break

print(ans)
