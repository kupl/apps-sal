from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float('inf')
(YES, Yes, yes, NO, No, no) = ('YES', 'Yes', 'yes', 'NO', 'No', 'no')
(dy4, dx4) = ([0, 1, 0, -1], [1, 0, -1, 0])
(dy8, dx8) = ([0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1])


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def sum_of_arithmetic_progression(s, d, n):
    return n * (2 * s + (n - 1) * d) // 2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def solve():
    (A, B, X) = list(map(int, input().split()))
    (low, high) = (-1, 10 ** 10)
    while high - low > 1:
        middle = (low + high) // 2
        need = A * middle + B * len(str(middle))
        if need <= X:
            low = middle
        else:
            high = middle
    low = min(max(0, low), 10 ** 9)
    print(low)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
