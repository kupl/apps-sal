import sys
from collections import deque
from bisect import bisect_left
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list((int(input()) for _ in range(n)))
    LIS = deque()
    for i in range(n):
        if len(LIS) == 0:
            LIS.appendleft(A[i])
        else:
            idx = bisect_left(LIS, A[i])
            if idx == 0:
                LIS.appendleft(A[i])
            else:
                LIS[idx - 1] = A[i]
    print(len(LIS))


def __starting_point():
    resolve()


__starting_point()
