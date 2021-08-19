# coding: utf-8
from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    ans = 0
    for value in list(c.values()):
        if value > 1:
            ans += value * (value - 1) // 2

    for i in range(N):
        print((ans - c[A[i]] + 1))


def __starting_point():
    main()


__starting_point()
