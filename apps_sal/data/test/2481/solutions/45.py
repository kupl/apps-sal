import sys
import math
from collections import deque
sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline()[:-1]


def mi():
    return map(int, input().split())


def ii():
    return int(input())


def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    H, W = mi()
    c = [list(mi()) for i in range(10)]
    A = [list(mi()) for i in range(H)]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                # i→k→j
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    ans = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] == -1:
                continue

            ans += c[A[h][w]][1]

    print(ans)


def __starting_point():
    main()


__starting_point()
