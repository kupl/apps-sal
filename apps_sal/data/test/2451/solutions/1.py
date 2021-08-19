import sys
import os


def solve(a, b, t1, f1, t2, f2):
    if t1 == t2:
        return abs(f1 - f2)
    elif f1 >= a and f1 <= b or (f2 >= a and f2 <= b):
        return abs(t1 - t2) + abs(f1 - f2)
    elif f1 > b and f2 > b:
        return abs(t1 - t2) + f1 + f2 - 2 * b
    elif f1 < a and f2 < a:
        return abs(t1 - t2) + 2 * a - f1 - f2
    else:
        return abs(t1 - t2) + abs(f1 - f2)


def main():
    (n, h, a, b, k) = map(int, input().split())
    for i in range(k):
        (t1, f1, t2, f2) = map(int, input().split())
        print(solve(a, b, t1, f1, t2, f2))


def __starting_point():
    main()


__starting_point()
