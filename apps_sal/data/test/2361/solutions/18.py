import sys
import random
import math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def main():
    inf = 10 ** 20

    t = int(input())

    for _ in range(1, t + 1):

        n, m, k = map(int, input().split())
        each = n // k
        best = min(each, m)
        m -= min(each, m)
        sec = m // (k - 1)
        if(m % (k - 1)):
            sec += 1
        print(best - sec)


main()
