import math
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions import gcd
n = int(input())
d = list(map(int, input().split()))
d.sort()
if d[n // 2] - d[n // 2 - 1] == 0:
    print(0)
else:
    print(d[n // 2] - d[n // 2 - 1])
