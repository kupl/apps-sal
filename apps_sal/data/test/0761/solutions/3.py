import sys
import os


def solve(slimes):
    if len(slimes) == 1:
        return slimes[0]

    havePos = False
    haveNeg = False

    for s in slimes:
        if s > 0:
            havePos = True
        elif s < 0:
            haveNeg = True

    if havePos and haveNeg:
        return sum(map(abs, slimes))
    elif not havePos:
        m = max(slimes)
        return sum(list(map(abs, slimes))) + 2 * m
    elif not haveNeg:
        m = min(slimes)
        return sum(list(map(abs, slimes))) - 2 * m
    else:
        return 0


def main():
    n = int(input())
    slimes = list(map(int, input().split()))
    print(solve(slimes))


def __starting_point():
    main()


__starting_point()
