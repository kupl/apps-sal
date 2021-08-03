#!/usr/bin/env python3

def solve():
    N = int(input())
    M = int(input())
    sizes = [int(input()) for _ in range(N)]

    sizes.sort(reverse=True)

    cnt = 0
    while M > 0:
        M -= sizes[cnt]
        cnt += 1
    print(cnt)


def __starting_point():
    solve()


__starting_point()
