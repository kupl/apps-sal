import numpy as np
import sys
sys.setrecursionlimit(10 ** 9)


def int1(x):
    return int(x) - 1


def II():
    return int(input())


def MI():
    return list(map(int, input().split()))


def MI1():
    return list(map(int1, input().split()))


def LI():
    return list(map(int, input().split()))


def LI1():
    return list(map(int1, input().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def MS():
    return input().split()


def LS():
    return list(input())


def LLS(rows_number):
    return [LS() for _ in range(rows_number)]


def printlist(lst, k=' '):
    print(k.join(list(map(str, lst))))


INF = float('inf')


def solve():
    (H, W) = MI()
    dist = LLI(10)
    N = 10
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for i in range(H):
        for r in LI():
            if r != -1:
                ans += dist[r][1]
    print(ans)


def __starting_point():
    solve()


__starting_point()
