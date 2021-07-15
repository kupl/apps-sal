import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, X = NMI()
    A = [1]
    P = [1]
    for i in range(N):
        A.append(A[-1]*2+3)
        P.append(P[-1]*2+1)

    def rec(n, x):
        if n == 0:
            return 1

        if x == 1:
            return 0
        elif x <= A[n-1]+1:
            return rec(n-1, x-1)
        elif x == A[n-1]+2:
            return P[n-1]+1
        elif x <= A[n]-1:
            return P[n-1]+1+rec(n-1, x-A[n-1]-2)
        else:
            return P[n]

    print(rec(N, X))


def __starting_point():
    main()
__starting_point()
