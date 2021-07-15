import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    n, m = list(map(int, readline().rstrip().split()))
    cnt = 2 ** m
    print(((n + m * 18) * cnt * 100))


def __starting_point():
    main()

__starting_point()
