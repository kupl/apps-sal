import sys
import itertools


def swap_rev(x, i, rev):
    if rev:
        (x[i], x[len(x) - i - 1]) = (x[len(x) - i - 1], x[i])


def main():
    s = sys.stdin.readline().strip()
    result = list(s)
    sys.stdin.readline()
    m = sorted(map(int, sys.stdin.readline().split()))
    rev = False
    prev = -1
    for (day, elements) in itertools.groupby(m):
        if len(list(elements)) % 2 == 0:
            continue
        day = day - 1
        for i in range(prev + 1, day):
            swap_rev(result, i, rev)
        rev = not rev
        swap_rev(result, day, rev)
        prev = day
    for i in range(prev + 1, int((len(result) + 1) / 2)):
        swap_rev(result, i, rev)
    print(''.join(result))


def __starting_point():
    main()


__starting_point()
