import bisect
import heapq
import itertools
import sys
import math
import random
import time
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor
from types import FunctionType
from typing import List

mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, input().split()))


def main():
    N = int(input())
    L = lmi()
    L.sort()
    ans = sum(L[::2])
    print(ans)


def __starting_point():
    main()


__starting_point()
