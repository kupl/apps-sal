import decimal
import itertools
import math
import functools
import bisect
import heapq
import random
from collections import Counter, deque, defaultdict
import time

# mod = 10 ** 9 + 7
mod = 1000000007


def lmi():
    return list(map(int, input().split()))


def main():
    N = int(input())
    S1 = input()
    S2 = input()

    prev = 0
    ans = 1
    next_skip = False
    for i in range(N):
        if next_skip:
            next_skip = False
            continue

        if S1[i] == S2[i]:
            ans *= 3 - prev
            prev = 1
        else:
            if prev == 1:
                ans *= 2
            elif prev == 2:
                ans *= 3
            else:
                ans *= 3 * 2
            prev = 2
            next_skip = True
    print((ans % mod))


def __starting_point():
    main()


__starting_point()
