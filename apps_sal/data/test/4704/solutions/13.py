import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = f_inf
    R = [0] + list(accumulate(A))
    for i in range(1, n):
        s = R[i] - R[0]
        a = R[-1] - R[i]
        diff = abs(s - a)
        res = min(res, diff)
    print(res)


def __starting_point():
    resolve()


__starting_point()
