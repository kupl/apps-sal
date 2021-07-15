import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")

    arr = []
    arr.extend(lst[::2])
    arr.extend(lst[1::2])
    arr.extend(lst[::2])
    arr.extend(lst[1::2])

    psum = []
    ps = 0
    for i in arr:
        ps += i
        psum.append(ps)
    
    res = 0
    sub_length = (len(lst)+1)//2
    # console(psum, sub_length)
    for i in range(len(lst)):
        res = max(res, psum[i+sub_length] - psum[i])

    # return a string (i.e. not a list or matrix)
    return res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
_ = int(input())
    
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

