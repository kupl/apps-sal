import math
import sys
import re
import itertools
import pprint
import collections
import copy
(rs, ri, rai, raf) = (input, lambda: int(input()), lambda: list(map(int, input().split())), lambda: list(map(float, input().split())))
t = input()
res = {t}
for i in range(52):
    t = t[-1] + t[:-1]
    res.add(t)
print(len(res))
