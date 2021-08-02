import sys


def solve():
    input = sys.stdin.readline
    X, Y = map(int, input().split())
    if abs(X - Y) > 1: print("Alice")
    else: print("Brown")

    return 0


def __starting_point():
    solve()


__starting_point()
