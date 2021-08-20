import math
import sys
import os
from operator import mul
sys.setrecursionlimit(10 ** 7)


def _S():
    return sys.stdin.readline().rstrip()


def I():
    return int(_S())


def LS():
    return list(_S().split())


def LI():
    return list(map(int, LS()))


if os.getenv('LOCAL'):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    sys.stdin = open(inputFile, 'r')
INF = float('inf')
N = I()
A = LI()
A.sort(reverse=True)
(half, isOdd) = divmod(len(A), 2)
ans = A[0]
for i in range(1, half):
    ans += 2 * A[i]
if isOdd == 1:
    ans += A[half]
print(ans)
