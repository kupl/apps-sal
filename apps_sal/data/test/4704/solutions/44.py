from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import product, combinations,permutations
from copy import deepcopy
import sys
sys.setrecursionlimit(4100000)



def __starting_point():
    N = int(input())
    A = list(map(int, input().split()))

    acc_A = []
    acc = 0
    for a in A:
        acc += a
        acc_A.append(acc)

    minv = 10e10
    for i in range(0, N-1):
        minv = min(abs(acc_A[i]-(acc_A[-1]-acc_A[i])), minv)
    print(minv)
__starting_point()
