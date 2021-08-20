import math
import sys
import re
import itertools
import pprint
import collections
import copy
(rs, ri, rai, raf) = (input, lambda: int(input()), lambda: list(map(int, input().split())), lambda: list(map(float, input().split())))
(n, a, b, c) = rai()
s = float('inf')
for ia in range(5):
    for ib in range(5):
        for ic in range(5):
            k = ia + 2 * ib + 3 * ic
            if (n + k) % 4 != 0:
                continue
            s = min(s, ia * a + ib * b + ic * c)
print(s)
