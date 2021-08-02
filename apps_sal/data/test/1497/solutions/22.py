__author__ = 'taras-sereda'
from collections import Counter


def b():
    n = int(input())

    mat = [input() for i in range(n)]
    return Counter(mat).most_common(1)[0][1]


def __starting_point():
    print(b())


__starting_point()
