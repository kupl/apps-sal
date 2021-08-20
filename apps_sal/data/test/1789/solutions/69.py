import sys
import math
import re
import random
import itertools
import bisect
from copy import copy
from collections import deque, Counter, defaultdict
from decimal import Decimal


def lcm(a, b):
    return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 9
(a, b, x, y) = map(int, input().split())
num = abs(a - b)
if a > b:
    print(min(x * (num * 2 - 1), x + y * (num - 1)))
elif a == b:
    print(x)
else:
    print(min(x * (num * 2 + 1), x + y * num))
