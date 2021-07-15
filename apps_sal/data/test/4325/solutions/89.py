import math
import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N, X, T = list(map(int, input().split()))
    print((math.ceil(N / X) * T))


def __starting_point():
    main()

__starting_point()
