#!/usr/bin/env python3

def main():
    n = int(input())
    v = sorted(map(int, input().split()))
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)


def __starting_point():
    main()


__starting_point()
