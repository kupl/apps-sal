import sys
sys.setrecursionlimit(10 ** 6)


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LC():
    return list(input())


def IC():
    return [int(c) for c in input()]


def MI():
    return map(int, input().split())


def solve():
    (N, M) = MI()
    if N == M == 1:
        print(1)
    elif N == 1:
        print(M - 2)
    elif M == 1:
        print(N - 2)
    else:
        print(N * M - (2 * N + 2 * M - 4))
    return


solve()
