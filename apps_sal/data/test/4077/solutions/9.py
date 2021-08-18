import math
import sys
from collections import defaultdict


def rt(): return list(map(int, input().split()))
def ri(): return int(input())
def rl(): return list(map(int, input().split()))


def main():
    n, m = rt()
    a = rl()

    def greaterCount(m):
        sums = defaultdict(int)
        s = n
        sums[s] = 1
        res = 0
        add = 0
        for i in range(n):
            if a[i] < m:
                s -= 1
                add -= sums[s]
            else:
                add += sums[s]
                s += 1
            res += add
            sums[s] += 1
        return res

    print(greaterCount(m) - greaterCount(m + 1))


def __starting_point():
    main()


__starting_point()
