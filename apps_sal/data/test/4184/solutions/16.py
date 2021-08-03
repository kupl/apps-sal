import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    W = list(map(int, input().split()))

    res = f_inf
    for i in range(n):
        left = sum(W[:i])
        right = sum(W[i:])
        res = min(res, abs(right - left))
    print(res)


def __starting_point():
    resolve()


__starting_point()
