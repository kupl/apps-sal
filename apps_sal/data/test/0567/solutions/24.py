import sys


def main():
    n = int(input())
    ar = list(map(int, input().split()))
    ar.extend([1, 10 ** 6])
    ar.sort()
    print(min([max(ar[i] - 1, 10 ** 6 - ar[i + 1]) for i in range(len(ar) - 1)]))


def __starting_point():
    main()


__starting_point()
