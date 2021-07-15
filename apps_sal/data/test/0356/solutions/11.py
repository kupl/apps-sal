import atexit
import io
import sys
# import os

# from bisect import *
# from collections import *
# from fractions import gcd
# from fractions import Fraction as fr_
# from itertools import *
# import math

inf = float('inf')  # sys.maxint in py2
inf_neg = float('-inf')  # sys.maxsize = 9*1e18
range_5 = int(1e5 + 1)
range_6 = int(1e6 + 1)
range_7 = int(1e7 + 1)
range_8 = int(1e8 + 1)
# sys.setrecursionlimit(range_8)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    # ll = list(map(int, input().split()))
    # print(f"{ ll }")
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    if sum(a) != sum(b):
        print(-1)
    else:
        i, j = 0, 0
        temp = 0
        while (i < n or j < m):
            if a[i] == b[j]:
                temp += 1
                if (i < n and j < m):
                    i += 1
                    j += 1
                else:
                    break
            elif (a[i] < b[j] and (i + 1) < n):
                a[i + 1] += a[i]
                i += 1
            elif (a[i] < b[j] and (i + 1) > n - 1):
                temp += 1
                break
            elif (a[i] > b[j] and (j + 1) < m):
                b[j + 1] += b[j]
                j += 1
            elif (a[i] > b[j] and (j + 1) > m - 1):
                temp += 1
                break
        print(temp)


def __starting_point():
    main()

__starting_point()
