import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    if N % 9 == 0:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
