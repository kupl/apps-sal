import math
from collections import Counter
from itertools import product


def ii(): return int(input())


def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


a, b, k = mi()

if a <= k:
    print(0, max(0, b - (k - a)))
else:
    print(a - k, b)
