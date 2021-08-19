import sys


def main():
    (c, v0, v1, a, l) = list(map(int, sys.stdin.readline().split()))
    day = 0
    v = v0
    read = 0
    while read < c:
        day += 1
        read = max(read - l, 0) + v
        v = min(v + a, v1)
    print(day)


def __starting_point():
    main()


__starting_point()
