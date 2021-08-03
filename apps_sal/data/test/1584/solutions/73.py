import bisect
from itertools import combinations


def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans = 0
    for l in combinations(L, 2):
        a = l[0]
        b = l[1]
        x = bisect.bisect_left(L, a + b)
        y = bisect.bisect(L, b - a)
        if b - a < a:
            ans += x - y - 2
        else:
            ans += x - y - 1
    print((ans // 3))


def __starting_point():
    main()


__starting_point()
