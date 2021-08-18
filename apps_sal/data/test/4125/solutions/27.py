
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

from functools import reduce


def gcd_list(numbers):
    return reduce(gcd, numbers)


N, X = [int(_) for _ in input().split()]
x = [int(_) for _ in input().split()]

if N != 1:
    ret = []
    x.append(X)
    now = x[0]

    for i in x[1:]:
        ret += [i - now]
        now = i

    ret = sorted(ret)

    print(gcd_list(ret))

else:
    print(abs(x[0] - X))
