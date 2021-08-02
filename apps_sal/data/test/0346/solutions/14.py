import sys
from itertools import *
from math import *
MAX = 10000000


def solve():
    n, m = list(map(int, input().split()))
    quest = list(map(int, input().split()))
    auctindex = set(map(int, input().split()))
    aucts = list()
    firstsum = 0
    for i, q in enumerate(quest):
        if (i + 1) not in auctindex:
            firstsum += q
        else:
            aucts.append(q)
    aucts.sort(reverse=True)
    for val in aucts:
        firstsum += max(firstsum, val)
    print(firstsum)


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
