import sys
import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n = inp()
n //= 2
n -= 1

print(math.factorial(2 * n + 1) // (n + 1))
