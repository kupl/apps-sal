# coding: utf-8

# https://atcoder.jp/contests/abc115
# 10:59 giveup


def main():
    N, X = list(map(int, input().split()))

    p = [None] * (N + 1)
    p[0] = 1
    for i in range(N):
        p[i + 1] = 2 * p[i] + 1

    whole = [None] * (N + 1)
    whole[0] = 1
    for i in range(N):
        whole[i + 1] = 2 * whole[i] + 3

    def rec(N, X):
        if N == 0:
            if X == 1:
                return 1
            else:
                return 0

        if X <= 1:
            return 0

        elif X <= 1 + whole[N - 1]:
            return rec(N - 1, X - 1)

        elif X <= 1 + whole[N - 1] + 1:
            return p[N - 1] + 1

        elif X <= 1 + whole[N - 1] + 1 + whole[N - 1]:
            return p[N - 1] + 1 + rec(N - 1, X - (1 + whole[N - 1] + 1))

        else:
            return p[N - 1] + 1 + p[N - 1]

    ans = rec(N, X)

    return ans


print((main()))
