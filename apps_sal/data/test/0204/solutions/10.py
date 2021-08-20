from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


(a, b, x, y) = readmap()
g = math.gcd(x, y)
print(min(a // (x // g), b // (y // g)))
