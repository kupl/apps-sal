import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")

    maxres = lst[0] * lst[1] * lst[2] * lst[3] * lst[4]

    if 0 in lst:
        maxres = max(maxres, 0)

    positives = sorted([a for a in lst if a >= 0])[::-1]
    negatives = sorted([a for a in lst if a < 0])

    if len(positives) >= 5 and len(negatives) >= 0:
        maxres = max(maxres, positives[0]* positives[1]* positives[2]* positives[3]* positives[4])

    if len(positives) >= 3 and len(negatives) >= 2:
        maxres = max(maxres, positives[0]* positives[1]* positives[2]* negatives[0]* negatives[1])

    if len(positives) >= 1 and len(negatives) >= 4:
        maxres = max(maxres, positives[0]* negatives[0]* negatives[1]* negatives[2]* negatives[3])

    if len(negatives) >= 5:
        maxres = max(maxres, negatives[-1]* negatives[-2]* negatives[-3]* negatives[-4]* negatives[-5])

    # return a string (i.e. not a list or matrix)
    return maxres


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)

