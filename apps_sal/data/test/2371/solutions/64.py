import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, z, w = list(map(int, input().split()))
    A = list(map(int, input().split()))

    res = abs(w - A[-1])
    if n > 1:
        res = max(res, abs(A[-2] - A[-1]))
    print(res)


def __starting_point():
    resolve()

__starting_point()
