import sys


def func(alst, sign):
    cur, res = 0, 0
    for i in alst:
        cur += i
        if sign and cur <= 0:
            res += abs(cur) + 1
            cur = 1
        elif not sign and cur >= 0:
            res += abs(cur) + 1
            cur = -1
        sign = not sign
    return res


def main():
    n, *alst = map(int, sys.stdin.read().split())
    print(min(func(alst, True), func(alst, False)))


def __starting_point():
    main()


__starting_point()
