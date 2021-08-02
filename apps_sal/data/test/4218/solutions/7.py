import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    cnt = 0
    for i in range(1, n + 1):
        if i % 2:
            cnt += 1
    print((cnt / n))


def __starting_point():
    resolve()


__starting_point()
