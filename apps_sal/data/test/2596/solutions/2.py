import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor
from copy import deepcopy
from itertools import accumulate
from collections import Counter
import math
from functools import reduce
from bisect import bisect_right
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(x): print("debug: ", x, file=sys.stderr)


def main():
    n, k, m, t = mi()
    ans = [k - 1, n - k]
    for i in range(t):
        c, i = mi()
        if c == 1:
            if i <= ans[0] + 1:
                ans[0] += 1
            else:
                ans[1] += 1
        else:
            if i <= ans[0]:
                ans[0] -= i
            else:
                ans[1] = i - ans[0] - 1
        print(sum(ans) + 1, ans[0] + 1)


def __starting_point():
    main()


__starting_point()
