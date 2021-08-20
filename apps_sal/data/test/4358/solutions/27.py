import math
import collections
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


n = ii()
p = [ii() for i in range(n)]
p.sort()
p[-1] //= 2
print(sum(p))
