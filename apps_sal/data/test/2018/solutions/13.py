import math
import sys
input = sys.stdin.readline
(n, m, q) = list(map(int, input().split()))
GCD = math.gcd(n, m)
k = n // GCD
l = m // GCD


def div(x, y):
    if x == 1:
        return (y - 1) // k
    else:
        return (y - 1) // l


for testcases in range(q):
    (sx, sy, ex, ey) = list(map(int, input().split()))
    if div(sx, sy) == div(ex, ey):
        print('YES')
    else:
        print('NO')
