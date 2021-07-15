#!/usr/bin/env python3
def main():
    import numpy as np

    N = int(input())

    can = [1]
    limit = 100
    for i in range(1, limit):
        six = 6 ** i
        if six <= N:
            can.append(six)
        nine = 9 ** i
        if nine <= N:
            can.append(nine)
        if six > N and nine > N:
            break

    INF = 10 ** 9
    dp = np.full(N + 1, INF, dtype=np.int32)
    dp[0] = 0
    for c in can:
        for _ in range(9):
            dp[c:] = np.minimum(dp[c:], dp[:-c] + 1)
    print((dp[-1]))


def __starting_point():
    main()

__starting_point()
