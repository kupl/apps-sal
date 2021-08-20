import sys
import re
import math
import collections
import itertools
import functools
DEBUG = True
DEBUG = False


def dbg(*args):
    if DEBUG:
        print('DBG: ', file=sys.stderr, end='')
        print(*args, file=sys.stderr)


def main():
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    candy_a = 0
    candy_b = 0
    for day in range(N):
        candy_a += A[day]
        if candy_a > 8:
            candy_b += 8
            candy_a -= 8
        else:
            candy_b += candy_a
            candy_a = 0
        if candy_b >= K:
            print(day + 1)
            return
    print(-1)


def __starting_point():
    main()


__starting_point()
