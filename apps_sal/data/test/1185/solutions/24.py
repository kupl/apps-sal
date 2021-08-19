import collections as col
import math
import sys
import math
input = sys.stdin.readline


def getInts():
    return [int(s) for s in input().split()]


def getInt():
    return int(input())


def getStrs():
    return [s for s in input().split()]


def getStr():
    return input().strip()


def listStr():
    return list(input().strip())


def solve():
    (N, M, K) = getInts()
    P = getInts()
    if M == 1:
        P.sort(reverse=True)
        return sum(P[:K])
    PP = [0]
    curr_sum = 0
    for p in P:
        curr_sum += p
        PP.append(curr_sum)
    dp = [[0 for j in range(N + 1)] for i in range(K + 1)]
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            if i * M > j:
                continue
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - M] + PP[j] - PP[j - M])
    return dp[K][N]


print(solve())
