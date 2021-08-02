# encoding: utf-8
import sys
sys.setrecursionlimit(10**6)


def __starting_point():
    # sys.stdin = open('1.std.in', 'r')
    nofkase = int(input())
    for kase in range(nofkase):
        n = int(input())
        n = n // 2
        print(n * (n + 1) * (n + n + 1) * 8 // 6)


__starting_point()
