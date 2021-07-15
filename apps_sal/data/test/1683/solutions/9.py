import sys
from collections import deque

IS_LOCAL = False


def read_one(dtype=int):
    return dtype(input())


def read_multiple(f, dtype=int):
    return f(list(map(dtype, input().split())))


def swap(x, y):
    return y, x


def main():
    n = 3
    a = [12, 3, 45]

    if not IS_LOCAL:
        n = read_one()
        a = read_multiple(list)

    d = 998_244_353
    s, k = 0, 1
    tot = n
    z = 0
    while tot > 0:
        zeroed = 0

        for i in range(n):
            if a[i] == 0:
                continue

            t = a[i] % 10
            a[i] //= 10
            if a[i] == 0:
                zeroed += 1

            s = (s + t * z * k * 2) % d
            s = (s + t * tot * k * k * 11) % d

        k *= 10
        z += k * zeroed
        tot -= zeroed

    print(s)

def __starting_point():
    if len(sys.argv) > 1 and sys.argv[1] == 'True':
        IS_LOCAL = True
    main()

__starting_point()
