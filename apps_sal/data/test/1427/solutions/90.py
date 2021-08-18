import sys
import math
import fractions
from collections import defaultdict
from functools import reduce
stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


INF = 10**18
mod = 10**9 + 7
N = int(input())
A = nl()
ans = 0
min_bai = 1

lcm = reduce(lambda x, y: x // fractions.gcd(x, y) * y, A)


ans = sum(lcm // x for x in A)
print((ans % mod))
