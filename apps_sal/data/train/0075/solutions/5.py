import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    t = 2 * n
    x = math.pi / (2 * t)
    h = 0.5 / math.sin(x)
    print(round(h, 7))
