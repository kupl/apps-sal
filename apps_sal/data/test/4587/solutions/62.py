from itertools import accumulate
from bisect import bisect, bisect_left
import sys
read = sys.stdin.read


def main():
    data = list(map(int, read().split()))
    n = data[0]
    a = data[1:n + 1]
    b = data[n + 1: n * 2 + 1]
    c = data[n * 2 + 1:]
    a.sort()
    b.sort()
    c.sort()
    b2 = [bisect_left(a, be) for be in b]
    b2a = list(accumulate(b2))
    b2a = [0] + b2a
    ans = sum([b2a[bisect_left(b, ce)] for ce in c])
    print(ans)


def __starting_point():
    main()


__starting_point()
