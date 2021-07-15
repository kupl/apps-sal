import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    X, Y, A, B, C = list(map(int, input().split()))
    P = sorted(list(map(int, input().split())), reverse=True)[:X]
    Q = sorted(list(map(int, input().split())), reverse=True)[:Y]
    R = sorted(list(map(int, input().split())), reverse=True)
    L = sorted(P + Q + R, reverse=True)
    res = sum(L[:X + Y])
    print(res)


def __starting_point():
    resolve()

__starting_point()
