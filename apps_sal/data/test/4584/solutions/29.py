from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
n = int(input())
A = list(map(int, input().split()))
b = [0] * (n + 1)
for i in A:
    b[i] += 1
for i in range(1, n + 1):
    print(b[i])
