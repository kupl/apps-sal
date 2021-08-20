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
        (N, S) = tuple(map(int, input().split()))
        if sum((int(dig) for dig in str(N))) <= S:
            print('0')
            continue
        str_N = '0' + str(N)
        total = 0
        i = 0
        while total < S:
            total += int(str_N[i])
            i += 1
        target = (int(str_N[:i - 1]) + 1) * 10 ** (len(str_N) - i + 1)
        print(str(target - N))


__starting_point()
