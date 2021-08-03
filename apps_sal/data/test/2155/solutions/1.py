import sys
from collections import Counter
from itertools import chain


def i_ints():
    return map(int, sys.stdin.readline().split())


def check(w, h, x, y, c):
    counts = Counter(chain.from_iterable(range(abs(i - x), abs(i - x) + y) for i in range(1, w + 1)))
    counts += Counter(chain.from_iterable(range(abs(i - x) + 1, abs(i - x) + 1 + (h - y)) for i in range(1, w + 1)))
    return c == counts


t, = i_ints()
a = Counter(i_ints())

i = 0
for i in range(1, t + 1):
    if a[i] != 4 * i:
        break
x = i
B = max(a)


def main():

    for w in range(2 * x - 1, int(t**0.5) + 2):
        if t % w:
            continue
        h = t // w

        y = w + h - B - x
        if y >= x and h >= 2 * y - 1 and check(w, h, x, y, a):
            return "%s %s\n%s %s" % (w, h, x, y)

        w, h = h, w
        y = w + h - B - x
        if y >= x and h >= 2 * y - 1 and check(w, h, x, y, a):
            return "%s %s\n%s %s" % (w, h, x, y)

    return -1


print(main())
