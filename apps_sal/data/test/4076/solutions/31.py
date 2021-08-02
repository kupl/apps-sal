from collections import Counter
import sys
import math

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)


def main():
    a, b, h, m = list(map(int, input().split()))
    x1 = a * math.cos(2 * math.pi * (h % 12 / 12 + m / 60 / 12))
    y1 = a * math.sin(2 * math.pi * (h % 12 / 12 + m / 60 / 12))
    x2 = b * math.cos(2 * math.pi * (m / 60))
    y2 = b * math.sin(2 * math.pi * (m / 60))

    print((((x1 - x2)**2 + (y1 - y2)**2)**(1 / 2)))


main()
