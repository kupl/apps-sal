import sys
import atexit
import io
from collections import defaultdict, Counter


def main():
    i = bin(int(input()))[2:]
    i = ('0' * (6 - len(i))) + i
    i = ''.join(list(map(lambda x: i[x], [0, 5, 3, 2, 4, 1])))
    print(int(i, 2))


def __starting_point():
    main()


__starting_point()
