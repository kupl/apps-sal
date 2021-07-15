import sys
from math import gcd, factorial, ceil, floor, sqrt
from bisect import bisect_left, bisect_right
from copy import deepcopy
from heapq import heapify, heappop, heappush
from itertools import permutations, combinations, product, accumulate
from collections import defaultdict, deque, Counter
from functools import lru_cache
sys.setrecursionlimit(10**8)

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

a, b = mi()
print((a+b)//2, (a-b)//2)
