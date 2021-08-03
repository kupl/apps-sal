#!/usr/bin/env python3

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        l, r = list(map(int, input().split()))
        ans += r - l + 1
    print(ans)


def __starting_point():
    main()


__starting_point()
