import sys
import random
import math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def main():
    inf = 10 ** 18
    t = int(input())
    for _ in range(1, t + 1):
        n = int(input())
        a = sorted([int(x) for x in input().split()])
        (l, r) = (-1, 0)
        ans = 0
        while r < n:
            if r - l + ans >= a[r]:
                ans += r - l
                l = r
            r += 1
        print(ans + 1)


main()
