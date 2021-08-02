import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    D, T, S = list(map(int, input().split()))
    if D / S <= T:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
