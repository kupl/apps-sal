#!/usr/bin/env python3
def main():
    H = int(input())

    res = 1
    ans = 1
    while H > 1:
        res *= 2
        ans += res
        H //= 2
    print(ans)


def __starting_point():
    main()

__starting_point()
