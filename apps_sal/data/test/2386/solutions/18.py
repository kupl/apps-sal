import bisect
import heapq
import itertools
import sys
import math
import random
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor
from typing import List

mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, input().split()))


def main():
    N = int(input())
    A = lmi()
    A_dash = [a - (i + 1) for i, a in enumerate(A)]
    A_dash.sort()
    b = A_dash[N // 2]
    ans = sum(abs(a - b) for i, a in enumerate(A_dash))

    print(ans)




def __starting_point():
    main()


__starting_point()
