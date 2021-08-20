import sys
from math import gcd
from functools import reduce
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, *A) = list(map(int, read().split()))
    print(reduce(gcd, A))
    return


def __starting_point():
    main()


__starting_point()
