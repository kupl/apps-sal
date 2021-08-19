import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr):  # fix inputs here
    console("----- solving ------")

    for candidate in range(512):
        for a in arr:
            for b in brr:
                if a & b | candidate == candidate:
                    break
            else:
                break
        else:
            return candidate


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())

    # read one line and parse each word as a string
    # lst = input().split()


    # read one line and parse each word as an integer
_ = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

# read matrix and parse as integers (after reading read nrows)
# lst = list(map(int,input().split()))
# nrows = lst[0]  # index containing information, please change
# grid = []
# for _ in range(nrows):
#     grid.append(list(map(int,input().split())))

res = solve(arr, brr)  # please change

# Google - case number required
# print("Case #{}: {}".format(case_num+1, res))

# Codeforces - no case number required
print(res)
