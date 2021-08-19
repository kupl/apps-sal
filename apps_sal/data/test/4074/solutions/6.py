import sys
import heapq
import random
import collections

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


from functools import reduce


def all_divisors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in
                       range(1, int(n**0.5) + 1) if n % i == 0)))


def solve(n, k):  # fix inputs here
    lst = all_divisors(n)
    # print(lst)
    lst = sorted(list(lst))
    for i in lst[::-1]:
        if i <= k:
            return n // i
    return n


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # _ = int(input())

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # _,_ = list(map(int,input().split()))
    n, k = list(map(int, input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(input()))

    res = solve(n, k)  # please change

    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
