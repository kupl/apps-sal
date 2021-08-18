import bisect
import collections


def solution():

    n = input().strip()

    if int(n[-1]) % 2 == 0:
        print("0")
    else:
        print("1")


def main():
    for _ in range(1):
        solution()


def __starting_point():
    main()


__starting_point()
