from sys import stdin
from math import cos,sin,radians
import math
inp = lambda: stdin.readline().strip()

# [int(x) for x in inp().split()]


def diagonal(x):
    return 1/(2*sin(radians(90/x)))


t = int(inp())
for _ in range(t):
    n = int(inp())
    # f = (diagonal(2*n)**2)**(1/2)
    print(diagonal(2*n))
