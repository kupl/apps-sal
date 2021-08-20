import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations, combinations, accumulate
from operator import itemgetter
from bisect import bisect_left, bisect
from heapq import heappop, heappush, heapify
from math import ceil, floor, sqrt
from copy import deepcopy


def main():
    num = list(map(int, input().split()))
    num.sort(reverse=True)
    print(num[0] * 10 + num[1] + num[2])


def __starting_point():
    main()


__starting_point()
