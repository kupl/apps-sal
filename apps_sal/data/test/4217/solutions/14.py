#!/usr/bin/env python3

def main():
    n, m = list(map(int, input().split()))
    k, *a = list(map(int, input().split()))
    ans = set(a)
    for i in range(n - 1):
        k, *a = list(map(int, input().split()))
        ans = ans & set(a)
    print((len(ans)))


def __starting_point():
    main()

__starting_point()
