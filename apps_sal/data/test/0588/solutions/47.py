import sys
from operator import itemgetter
import math
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def main():
    N = int(input())
    XY = [[int(x) for x in input().split()] for _ in range(N)]
    ans = 0
    for (i, (x, y)) in enumerate(XY):
        if x == 0:
            katamuki = 1 / 10 ** 7
            katamuki2 = -1 / 10 ** 7
        else:
            katamuki = y / x + 1 / 10 ** 7
            katamuki2 = y / x - 1 / 10 ** 7
        plus = [0, 0]
        minus = [0, 0]
        plus2 = [0, 0]
        minus2 = [0, 0]
        for (j, (xx, yy)) in enumerate(XY):
            if yy > katamuki * xx:
                plus[0] += xx
                plus[1] += yy
            else:
                minus[0] += xx
                minus[1] += yy
            if yy > katamuki2 * xx:
                plus2[0] += xx
                plus2[1] += yy
            else:
                minus2[0] += xx
                minus2[1] += yy
        ans = max(ans, math.sqrt(plus[0] ** 2 + plus[1] ** 2))
        ans = max(ans, math.sqrt(minus[0] ** 2 + minus[1] ** 2))
        ans = max(ans, math.sqrt(plus2[0] ** 2 + plus2[1] ** 2))
        ans = max(ans, math.sqrt(minus2[0] ** 2 + minus2[1] ** 2))
    print(ans)


def __starting_point():
    main()


__starting_point()
