from bisect import bisect
from itertools import accumulate
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    (n, m, k) = map(int, input().split())
    a = tuple(accumulate(map(int, input().split())))
    b = tuple(accumulate(map(int, input().split())))
    r = bisect(b, k)
    for (i1, ae) in enumerate(a):
        if k < ae:
            break
        r = max(r, bisect(b, k - ae) + i1 + 1)
    print(r)


def __starting_point():
    main()


__starting_point()
