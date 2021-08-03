import sys
import math
import random
from fractions import gcd
from itertools import permutations

debug = 0
if debug:
    f = open("input.txt", "r")
    input = f.readline
else:
    input = sys.stdin.readline


def mp():
    return list(map(int, input().split()))


def _main():
    n = int(input())
    a = mp()
    b = mp()
    if sum(a) < sum(b):
        print("No")
    else:
        print("Yes")


_main()
