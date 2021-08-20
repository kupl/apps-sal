import sys
from itertools import product
input = sys.stdin.readline


def main():
    (n, z, w) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = abs(w - a[-1])
    if n != 1:
        ans = max(ans, abs(a[-2] - a[-1]))
    print(ans)


def __starting_point():
    main()


__starting_point()
