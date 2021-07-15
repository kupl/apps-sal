# -*- coding: utf-8 -*-


def rli():
    return list(map(int, input().split()))


def main():
    n, k = rli()
    ans = n * 3
    if k != n and k != 1:
        ans += min(n - k, k - 1)
    print(ans)


def __starting_point():
    main()

__starting_point()
