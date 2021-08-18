from sys import stdin
import math
from collections import defaultdict


I = stdin.readline


s = []
for i in range(1, 10000):
    s.append(str(i))

s = "".join(s)

n = int(I())
print(s[n - 1])
