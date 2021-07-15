import sys

input = sys.stdin.readline


def main():
    A, B = list(map(int, input().split()))
    if B % A == 0:
        print((A + B))
    else:
        print((B - A))


def __starting_point():
    main()

__starting_point()
