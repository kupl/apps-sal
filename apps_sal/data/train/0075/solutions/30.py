from sys import stdin
from math import cos, sin, radians
import math
def inp(): return stdin.readline().strip()


def diagonal(x):
    return 1 / (2 * sin(radians(90 / x)))


t = int(inp())
for _ in range(t):
    n = int(inp())
    print(diagonal(2 * n))
