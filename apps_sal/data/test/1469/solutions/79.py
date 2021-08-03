import sys

input = sys.stdin.readline


def main():
    L = int(input())

    Lstr = bin(L)[2:]

    N = len(Lstr)
    M = (N - 1) * 2 + (Lstr.count("1") - 1)

    print((N, M))
    c = 1
    for i in range(1, N):
        print((i, i + 1, c))
        print((i, i + 1, 0))
        c *= 2

    c = 2 ** (N - 1)
    for i, v in enumerate(Lstr[::-1]):
        if i == N - 1:
            continue
        if v == "1":
            print((i + 1, N, c))
            c += 2 ** i


def __starting_point():
    main()


__starting_point()
