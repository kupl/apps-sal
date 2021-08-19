import sys
from math import *
sys.setrecursionlimit(10 ** 6)


def main():
    n = int(input())
    en = []
    n0 = n
    for _ in range(n0):
        (x, y) = list(map(int, input().split()))
        if (x, y) == (0, 0):
            n -= 1
            continue
        en.append([atan2(y, x), x, y])
    en.sort()
    ans = 0
    for l in range(n):
        sx = sy = 0
        arg_l = en[l][0]
        r = l
        for _ in range(n):
            if (en[r][0] - arg_l) % (2 * pi) > pi:
                break
            sx += en[r][1]
            sy += en[r][2]
            ans = max(ans, sx ** 2 + sy ** 2)
            r = (r + 1) % n
    print(ans ** 0.5)


main()
