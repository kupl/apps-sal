# -*- coding: utf-8 -*-


def rli():
    return list(map(int, input().split()))


def main():
    n = int(input())
    ns = []
    for i in range(n):
        x, y = rli()
        ns.append((x, y))
    w = int(input())
    for i in range(n):
        x, y = ns[i]
        if y >= w:
            print(n - i)
            return


def __starting_point():
    main()


__starting_point()
