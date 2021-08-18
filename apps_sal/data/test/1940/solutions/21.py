from collections import deque
from sys import stdin
from math import ceil
lines = deque(line.strip() for line in stdin.readlines())


def nextline():
    return lines.popleft()


def types(cast):
    return tuple(int(x) for x in nextline().split())


def ints():
    return types(int)


def strs():
    return nextline().split()


def main():
    n, k = ints()
    ws = ints()
    count = ceil(sum(ceil(x / k) for x in ws) / 2)
    print(count)


def __starting_point():
    main()


__starting_point()
