from functools import reduce
from operator import mul
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def main():
    (n, k) = list(map(int, input().split()))
    modulo = 1000000000 + 7

    def cmb(n, r):
        if n < r:
            return 0
        r = min(n - r, r)
        if r == 0:
            return 1
        numer = reduce(mul, range(n, n - r, -1))
        denom = reduce(mul, range(1, r + 1))
        return numer // denom % modulo
    for i in range(1, k + 1):
        a = cmb(k - 1, i - 1)
        b = cmb(n - k + 1, i)
        print(a * b % modulo)


main()
