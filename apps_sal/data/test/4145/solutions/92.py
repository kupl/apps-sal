from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement


def is_prime(t):
    k = 2
    while k * k <= t:
        if t % k == 0:
            return False
        k += 1
    return True


x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1
