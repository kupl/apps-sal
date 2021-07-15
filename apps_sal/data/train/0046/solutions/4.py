import sys
import math
import collections
import heapq

def set_debug(debug_mode=False):
    if debug_mode:
        fin = open('input.txt', 'r')
        sys.stdin = fin


def int_input():
    return list(map(int, input().split()))


def __starting_point():
    # set_debug(True)

    t = int(input())
    # t = 1

    for ti in range(1, t + 1):
        # n = int(input())
        s = input()

        c = collections.Counter(s)
        m = max(c['R'], c['S'], c['P'])

        if m == c['R']:
            print('P' * len(s))
        elif m == c['S']:
            print('R' * len(s))
        else:
            print('S' * len(s))

__starting_point()
