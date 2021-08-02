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
    n = int(input())

    if n == 0:
        print(0)
        return

    ans = ""
    while n:
        if n % 2:
            n -= 1
            ans += "1"
        else:
            ans += "0"
        n //= (-2)

    print(ans[::-1])


def __starting_point():
    main()


__starting_point()
