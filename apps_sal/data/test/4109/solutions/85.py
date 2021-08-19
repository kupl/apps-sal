from itertools import product
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
#import numpy as np


def main():
    n, m, x = list(map(int, input().split()))
    books = []
    for _ in range(n):
        books.append(tuple(map(int, input().split())))
    p = tuple(product((0, 1), repeat=n))
    r = float('inf')
    for pe in p:
        effects = [0] * (m + 1)
        for i1 in range(n):
            if pe[i1]:
                for i2 in range(m + 1):
                    effects[i2] += books[i1][i2]
        if all([e >= x for e in effects[1:]]):
            r = min(r, effects[0])
    if r == float('inf'):
        print((-1))
    else:
        print(r)


def __starting_point():
    main()


__starting_point()
