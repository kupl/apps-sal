import math
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)


def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int, LS()))


if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

# N = I()
# a = LI()

A, B, C, D = LI()

if B <= C or D <= A:
    ans = 0
elif C <= A and B <= D:
    ans = B - A
elif A <= C and D <= B:
    ans = D - C
elif A <= C and B <= D:
    ans = B - C
elif C <= A and D <= B:
    ans = D - A
else:
    ans = 'error'

print(ans)
