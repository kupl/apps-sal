import math
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions import gcd
(a, b, c) = map(int, input().split())
l = [a, b, c]
l.sort()
cnt = l[2] - l[1]
c = math.ceil((l[2] - (l[0] + cnt)) / 2)
if l[0] + 2 * c + cnt == l[2]:
    print(cnt + c)
else:
    print(cnt + c + 1)
