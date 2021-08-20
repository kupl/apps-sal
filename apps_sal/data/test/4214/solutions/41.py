from math import factorial
from itertools import permutations
import sys
3


def input():
    return sys.stdin.readline().strip()


n = int(input())
coords = [[int(x) for x in input().split()] for _ in range(n)]
print(f'{sum((((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5 for p in permutations(coords) for (i, j) in zip(p, p[1:]))) / factorial(n):.6f}')
