import sys
from itertools import *
from math import *
MAX = 10000000


def solve():
    n, m, ss, ll = list(map(int, input().split()))
    a = set(map(int, input().split()))
    wantothers = 0
    smallest = 100000000
    largest = -1
    for val in a:
        smallest = min(smallest, val)
        largest = max(largest, val)
    if smallest < ss or largest > ll:
        print("Incorrect")
        return
    if ss not in a:
        wantothers += 1
    if ll not in a:
        wantothers += 1
    print("Correct" if wantothers <= n - m else "Incorrect")


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
