import sys
from collections import defaultdict, Counter
import string


def main():
    (n, c) = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]
    words = 1
    for (i, j) in zip(t[:-1], t[1:]):
        if j - i > c:
            words = 1
        else:
            words += 1
    print(words)


def __starting_point():
    main()


__starting_point()
