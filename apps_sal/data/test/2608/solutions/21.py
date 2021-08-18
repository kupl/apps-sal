from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
import sys
import math
MAX = sys.maxsize
MAXN = 10**6 + 10
MOD = 10**9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def numIN():
    return(list(map(int, sys.stdin.readline().strip().split())))


def charIN():
    return(sys.stdin.readline().strip().split())


def solve(x1, y1, x2, y2):
    xa = x2 - x1 + 1
    ya = y2 - y1 + 1

    area = xa * ya

    if(x1 + y1) % 2 == 0:
        if area % 2:
            tw = area // 2 + 1
        else:
            tw = area // 2
    else:
        tw = area // 2

    return area - tw, tw


for _ in range(int(input())):
    n, m = numIN()
    black = (n * m) // 2
    white = (n * m) - black
    x1, y1, x2, y2 = numIN()
    x3, y3, x4, y4 = numIN()
    b1, w1 = solve(x1, y1, x2, y2)
    black -= b1
    white += b1
    b2, w2 = solve(x3, y3, x4, y4)
    black += w2
    white -= w2
    x5 = max(x1, x3)
    y5 = max(y1, y3)
    x6 = min(x2, x4)
    y6 = min(y2, y4)
    ar = (x6 - x5 + 1) * (y6 - y5 + 1)
    b3, w3 = solve(x5, y5, x6, y6)
    if x5 <= x6 and y5 <= y6:
        black += b3
        white -= b3
    print(white, black)
