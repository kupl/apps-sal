import math
import sys


def main():
    n, d = list(map(int, input().split()))
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    k = (months[n - 1] - (8 - d))
    ans = 1 + k // 7 + int(k % 7 > 0)
    print(ans)


def __starting_point():
    main()


__starting_point()
