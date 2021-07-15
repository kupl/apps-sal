import sys
from operator import itemgetter
import math

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    XY = [[int(x) for x in input().split()] for _ in range(N)]

    txy = []
    for x, y in XY:
        t = math.atan2(y, x)
        txy.append([t, x, y])

    txy.sort()

    ans = 0
    for i in range(N):
        tmpx = 0
        tmpy = 0
        for j in range(N):
            tmpx += txy[(i + j) % N][1]
            tmpy += txy[(i + j) % N][2]
            ans = max(ans, math.sqrt(tmpx ** 2 + tmpy ** 2))


    print(ans)


def __starting_point():
    main()

__starting_point()
