import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (x, t) = list(map(int, input().split()))
    print(max(0, x - t))


def __starting_point():
    resolve()


__starting_point()
