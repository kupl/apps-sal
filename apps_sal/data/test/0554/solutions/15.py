import math
import sys
import re
import itertools
import pprint
import collections
import copy
rs, ri, rai, raf = input, lambda: int(input()), lambda: list(map(int, input().split())), lambda: list(map(float, input().split()))

n, m = rai()
a = rai()
b = [rai() for i in range(m)]
s = 0
for i, j in b:
    t = sum(a[i - 1:j])
    if t > 0:
        s += t

print(s)
