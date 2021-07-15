import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue
from functools import reduce

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    from functools import reduce

    # 最小公倍数
    def lcm_base(x, y):
        return (x * y) // math.gcd(x, y)

    def lcm_list(numbers):
        return reduce(lcm_base, numbers, 1)

    n = ni()
    a = na()

    lcm = a[0]
    for i in a:
        lcm = lcm // math.gcd(lcm, i) * i
    lcm %= MOD

    ans = 0
    for ai in a:
        ans += lcm * pow(ai, MOD - 2, MOD) % MOD
        ans %= MOD

    print(ans)


def __starting_point():
    main()

__starting_point()
