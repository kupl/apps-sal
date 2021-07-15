import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


MOD = 10 ** 9 + 7
sys.setrecursionlimit(20000000)
INF = float("inf")


def main():
    N, M = list(map(int, input().split()))
    key = []
    for _ in range(M):
        a, b = list(map(int, input().split()))
        C = list([int(x) - 1 for x in input().split()])
        state = 0
        for c in C:
            state += 2 ** c
        key.append((a, state))
    dp = [INF for _ in range(2 ** N)]
    dp[0] = 0
    for i in range(2 ** N - 1):
        for k in range(M):
            state = key[k][1]
            tmp = dp[i] + key[k][0]
            if dp[i | state] > tmp:
                dp[i | state] = tmp
    if dp[-1] == INF:
        print((-1))
    else:
        print((dp[-1]))


def __starting_point():
    main()

__starting_point()
