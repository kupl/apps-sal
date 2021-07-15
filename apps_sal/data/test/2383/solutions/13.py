#!/usr/bin/env python3
def main():
    N = int(input())
    a = [int(x) for x in input().split()]

    cnt = 0
    for num in a:
        if num == cnt + 1:
            cnt += 1
    if cnt == 0:
        print((-1))
    elif cnt == N:
        print((0))
    else:
        print((N - cnt))


def __starting_point():
    main()

__starting_point()
