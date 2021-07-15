import bisect
import copy
import fractions
import functools
import heapq
import math
import random
import sys


def __starting_point():

    T = int(input())

    for t in range(T):
        N, S = tuple(map(int, input().split()))

        if sum(int(dig) for dig in str(N)) <= S:
            print('0')
            continue

        # So we start counting digits from left to right
        # The first digits where the sum is greater than or equal to S and every digit following
        # needs to be set to 0, and the last digit we safely counted gets incremented
        # Our answer is the difference between this number and N

        str_N = '0' + str(N)

        total = 0
        i = 0
        while total < S:
            total += int(str_N[i])
            i += 1

        target = (int(str_N[:i-1]) + 1) * (10 ** (len(str_N) - i + 1))
        print(str(target - N))

__starting_point()
