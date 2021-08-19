#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


INF = float("inf")


def main():
    ans = 0
    N = INT()
    for i in range(N):
        ans += (N - i) * (N - i + 1) // 2
    uv = ZIP(N - 1)
    for u, v in uv:
        if v < u:
            u, v = v, u
        ans -= u * (N - v + 1)
    print(ans)

    return


def __starting_point():
    main()


__starting_point()
