import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    L = pow(2, N)
    Dist = [10 ** 20] * L

    Dist[0] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        bit = 0
        C = [int(c) for c in input().split()]
        for c in C:
            bit += pow(2, c - 1)
        for k in range(L):
            if Dist[k] < 10 ** 20:
                Dist[k | bit] = min(Dist[k | bit], Dist[k] + a)
    if Dist[L - 1] == 10 ** 20:
        print(-1)
    else:
        print(Dist[L - 1])

    return 0


def __starting_point():
    solve()


__starting_point()
