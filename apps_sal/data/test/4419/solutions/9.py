import sys
from math import ceil
fast_reader = sys.stdin.readline
fast_writer = sys.stdout.write


def input():
    return fast_reader().strip()


def print(*argv):
    fast_writer(' '.join((str(i) for i in argv)))
    fast_writer('\n')


for _ in range(int(input())):
    (a, b) = map(int, input().split())
    print(ceil(abs(a - b) / 10))
