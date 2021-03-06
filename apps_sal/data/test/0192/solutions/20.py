import sys


def read_data():
    return list(map(int, next(sys.stdin).split()))


def solve(f, t):
    if f > t:
        (f, t) = (t, f)
    if f == t:
        return 0
    (a, b, c) = (f, f, f)
    count = 0
    while a < t:
        c = min(a + b - 1, t)
        (c, b, a) = sorted((a, b, c))
        count += 1
    if b < t:
        count += 1
        if c < t:
            count += 1
    return count


def __starting_point():
    (f, t) = read_data()
    print(solve(f, t))


__starting_point()
