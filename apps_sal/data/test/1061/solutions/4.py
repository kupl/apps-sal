import sys
import math


def matrix():
    rows = 0
    matrix = []
    for i in range(5):
        matrix.append(input().split())
    for i in matrix:
        rows += 1
        if '1' in i:
            columns = i.index('1') + 1
            break
    print(abs(3 - rows) + abs(3 - columns))


matrix()
