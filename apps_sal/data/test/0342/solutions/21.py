import sys
import math
from itertools import permutations
input = sys.stdin.readline

a, b, c = map(int, input().split())

minn = min(a, b)
maxx = max(a, b)

if a != b:
    print(2 * c + 2 * minn + 1)
else:
    print(2 * c + 2 * minn)
