"""

created by huash06 at 2015-07-14

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools

# sys.stdin = open("input.txt", "r")


def collectApple(tree):
    if not tree:
        return 0
    left = sorted([x for x in tree if x[0] < 0])
    right = sorted([x for x in tree if x[0] > 0])

    res = 0
    if len(left) > len(right):
        res += sum([x[1] for x in right])
        res += sum([x[1] for x in left[len(left) - len(right) - 1:]])
    else:
        res += sum([x[1] for x in left])
        res += sum([x[1] for x in right[:min(len(left) + 1, len(right))]])
    return res


N = int(input())

tree = []
for i in range(N):
    tree.append([int(x) for x in input().split()])
print(collectApple(tree))
