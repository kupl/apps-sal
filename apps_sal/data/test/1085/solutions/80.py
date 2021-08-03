#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
# input=sys.stdin.readline
import bisect
n = int(input())
m = int(pow(n, 0.5))
s = set()
t = set()
for i in range(1, m + 1):
    if n % i == 0:
        s.add(i)
        s.add(n // i)
    if (n - 1) % i == 0:
        t.add(i)
        t.add((n - 1) // i)
ans = len(t) - 1
for i in s:
    if i == 1:
        continue
    c = n
    while True:
        if c % i == 0:
            c = c // i
        else:
            if c % i == 1:
                ans += 1
            break
print(ans)
