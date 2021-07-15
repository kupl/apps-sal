from collections import defaultdict
# from fractions import Fraction
def read_line():
    return [int(x) for x in input().split()]

n, k = read_line()

from math import ceil
print(sum(ceil(n*c/k) for c in  [2, 5, 8]))

