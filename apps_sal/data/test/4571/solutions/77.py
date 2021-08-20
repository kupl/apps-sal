from decimal import Decimal
from functools import lru_cache
from math import ceil
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from collections import deque
from math import sqrt
import sys
import math
import heapq
mod = 10 ** 9 + 7
inf = float('inf')


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)
(n, m) = list(map(int, input().split()))
A = 100 * (n - m) + 1900 * m
p = pow(2, m)


@lru_cache(maxsize=10 ** 10)
def per(n):
    if n == 1:
        return 1 / p
    return (1 - sum([per(i) for i in range(1, n)])) * (1 / p)


ans = 0
for i in range(1, 2000):
    ans += i * A * per(i)
print(round(ans))
