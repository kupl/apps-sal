import math
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

N = I()
A = LI()

A.sort(reverse=True)
# print(A)
# half = math.ceil(len(A)/2)
q, mod = divmod(len(A), 2)

if mod == 0:
    ans = A[0]
    for i in range(1, q):
        ans += 2 * A[i]
else:
    ans = A[0]
    for i in range(1, q):
        ans += 2 * A[i]
    ans += A[q]

print(ans)
