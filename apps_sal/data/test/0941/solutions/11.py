from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect
setrecursionlimit(10 ** 7)


def read():
    return int(input())


def reads():
    return [int(x) for x in input().split()]


(b, k) = reads()
a = reads()


def answer(n):
    print('even' if n % 2 == 0 else 'odd')
    return


if b % 2 == 0:
    answer(a[-1])
else:
    answer(sum(a))
