import math
from collections import Counter
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


(k, x) = mi()
if 500 * k >= x:
    print('Yes')
else:
    print('No')
