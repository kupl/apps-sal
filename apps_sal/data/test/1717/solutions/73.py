from itertools import accumulate, chain, combinations, groupby, permutations, product
from collections import deque, Counter
from bisect import bisect_left, bisect_right
from math import gcd, sqrt, sin, cos, tan, degrees, radians
from fractions import Fraction
from decimal import Decimal
from functools import reduce
import sys
def input(): return sys.stdin.readline().rstrip()


#from sys import setrecursionlimit
# setrecursionlimit(10**7)
MOD = 10**9 + 7
INF = float('inf')


def lcm_base(x, y):
    return (x * y) // gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())

print(1 + lcm(*list(range(2, n + 1))))
