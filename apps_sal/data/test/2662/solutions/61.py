import sys
from collections import deque
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))

    que = deque([A[0]])
    for i in range(1, n):
        idx = bisect_left(que, A[i])
        if idx == 0:
            que.appendleft(A[i])
        else:
            idx -= 1
            que[idx] = A[i]
    print((len(que)))


def __starting_point():
    resolve()

__starting_point()
