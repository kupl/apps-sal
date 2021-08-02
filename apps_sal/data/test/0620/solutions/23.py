import math
import sys
import re
import itertools
import pprint
import collections
import copy
rs, ri, rai, raf = input, lambda: int(input()), lambda: list(map(int, input().split())), lambda: list(map(float, input().split()))

a = rai()
b = rai()
c = rai()

bc = [c[0] - b[0], c[1] - b[1]]
ba = [a[0] - b[0], a[1] - b[1]]
ac = [c[0] - a[0], c[1] - a[1]]

sum2 = lambda a, b: tuple([a[0] + b[0], a[1] + b[1]])
inv = lambda a: [-a[0], -a[1]]

res = set()
res.add(sum2(a, bc))
res.add(sum2(a, inv(bc)))
res.add(sum2(b, ac))
res.add(sum2(b, inv(ac)))
res.add(sum2(c, ba))
res.add(sum2(c, inv(ba)))

print(len(res))
for x, y in res:
    print(x, y)
