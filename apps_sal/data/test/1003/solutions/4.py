import sys
3


def __starting_point():

    n, m = list(map(int, sys.stdin.readline().split()))
    d = 0
    while n > 0:
        d += 1
        n -= 1
        if d % m == 0:
            n += 1

    print(d)


__starting_point()
