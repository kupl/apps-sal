import math
#import itertools
#import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#MOD = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int, input().split())
STRM = lambda: map(str, input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int, input().split()))
LISTS = lambda: list(map(str, input().split()))


def do():
    a, b, c, d = INTM()
    lcm = (c * d) // math.gcd(c, d)
    a -= 1
    ct_a = a - (a // c) - (a // d) + (a // lcm)
    ct_b = b - (b // c) - (b // d) + (b // lcm)
    print(ct_b - ct_a)


def __starting_point():
    do()


__starting_point()
