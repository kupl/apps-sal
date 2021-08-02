import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    P = [int(p) for p in input().split()]
    diff = 0
    for i in range(N):
        if P[i] != i + 1: diff += 1
    if diff <= 2: print("YES")
    else: print("NO")

    return 0


def __starting_point():
    solve()


__starting_point()
