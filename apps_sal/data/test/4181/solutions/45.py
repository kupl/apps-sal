# -*-coding:utf-8-*-
import numpy as np
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    mob = np.array(list(map(int, input().split())), dtype=int)
    bra = np.array(list(map(int, input().split())), dtype=int)
    ans = 0

    for i in range(n):
        ans += min(mob[i], bra[i])
        ans += min(mob[i + 1], bra[i] - min(mob[i], bra[i]))
        mob[i + 1] -= min(mob[i + 1], bra[i] - min(mob[i], bra[i]))
    print(ans)


def __starting_point():
    main()


__starting_point()
