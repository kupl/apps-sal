import sys
input = sys.stdin.readline
from math import gcd
from functools import reduce


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    return reduce(gcd, A)


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print(("%s" % str(outputs)))

__starting_point()
