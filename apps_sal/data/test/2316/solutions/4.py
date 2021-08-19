from math import *


def _i():
    return [int(i) for i in input().split()]


def _f():
    return [int(i) for i in input().split()]


for zz in range(int(input())):
    (x, n, m) = _i()
    ans = 0
    while x // 2 + 10 < x and n > 0:
        ans += 1
        x = x // 2 + 10
        n -= 1
    while x > 0 and m > 0:
        x -= 10
        m -= 1
    if x <= 0:
        print('YES')
    else:
        print('NO')
