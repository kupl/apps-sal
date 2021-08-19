import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    (x, y, a, b, c) = list(map(int, input().split()))
    print(sum(sorted(sorted(list(map(int, input().split())), reverse=True)[0:x] + sorted(list(map(int, input().split())), reverse=True)[0:y] + sorted(list(map(int, input().split())), reverse=True), reverse=True)[0:x + y]))


def __starting_point():
    main()


__starting_point()
