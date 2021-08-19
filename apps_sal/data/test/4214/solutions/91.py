# coding: utf-8
from math import sqrt
from itertools import permutations


def main():
    N = int(input())
    ans = 0.0
    P = [i for i in range(N)]
    C = [list(map(int, input().split())) for _ in range(N)]
    for p in permutations(P):
        for i in range(N - 1):
            ans += sqrt(((C[p[i + 1]][0] - C[p[i]][0]) ** 2) + ((C[p[i + 1]][1] - C[p[i]][1]) ** 2))

    for i in range(2, N + 1):
        ans /= i

    print(ans)


def __starting_point():
    main()


__starting_point()
