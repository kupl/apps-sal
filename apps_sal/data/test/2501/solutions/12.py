# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    ans = 0

    for i in range(n):
        diff = i - a[i]
        ans += d[diff]

        summed = i + a[i]
        d[summed] += 1

    print(ans)


def __starting_point():
    main()

__starting_point()
