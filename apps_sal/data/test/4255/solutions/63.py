import math
import collections
from itertools import product

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

l = li()
l.sort()
print(l[0] * l[1] // 2)
