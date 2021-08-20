import sys


def main():
    (n, x) = tuple([int(y) for y in input().split()])
    c = 1
    out = 0
    for i in range(n):
        (l, r) = tuple([int(y) for y in input().split()])
        s = int((l - c) / x)
        if s > 0:
            c += x * s
        out += r - c + 1
        c = r + 1
    print(out)


def __starting_point():
    main()


__starting_point()
