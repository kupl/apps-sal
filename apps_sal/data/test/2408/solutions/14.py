from random import random
from collections import defaultdict
from fractions import Fraction
import math
import re
import fractions
N = int(input())
lines = defaultdict(set)
poles = []
for _ in range(N):
    (x, y) = list(map(int, input().split(' ')))
    for (xx, yy) in poles:
        if yy - y == 0:
            slope = Fraction(10 ** 6, 1)
            const = y
        else:
            slope = Fraction(xx - x, yy - y)
            const = x - slope * y
        lines[slope].add(const)
    poles.append((x, y))
result = 0
visited = 0
for slope in lines:
    result += visited * len(lines[slope])
    visited += len(lines[slope])
print(result)
